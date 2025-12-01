let calendarDays = document.querySelectorAll('.calendar')

// Get today's date
const today = new Date();

// Set target date (Dec 25, current year)
const year = today.getFullYear();
const christmas = new Date(year, 11, 25); // Month is 0-indexed (11 = December)

// Calculate days difference
const diffTime = christmas - today;
// convert milliseconds to days is what the below code is about
const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

const remainderDays = 25 - diffDays;

// loop through elements in calendar days and null days past
for (let i = 0; i < remainderDays && i < calendarDays.length; i++) {
    calendarDays[i].classList.remove('calendar');
    calendarDays[i].classList.add('calendar-mute');
}