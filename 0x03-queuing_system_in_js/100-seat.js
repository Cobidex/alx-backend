import express from 'express';
import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';

const app = express();
const client = redis.createClient();
const queue = kue.createQueue();

const reserveSeatAsync = promisify(client.set).bind(client);
const getCurrentAvailableSeatsAsync = promisify(client.get).bind(client);

const availableSeatsKey = 'available_seats';
let reservationEnabled = true;

reserveSeatAsync(availableSeatsKey, 50);

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeatsAsync(availableSeatsKey);
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }

    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentSeats = await getCurrentAvailableSeatsAsync(availableSeatsKey);
    const newSeats = currentSeats - 1;

    if (newSeats === 0) {
      reservationEnabled = false;
    }

    if (newSeats >= 0) {
      await reserveSeatAsync(availableSeatsKey, newSeats);
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});

const port = 1245;

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
