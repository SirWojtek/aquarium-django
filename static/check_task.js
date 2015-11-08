
day_to_number = {
    'M' : 1,
    'TU' : 2,
    'W' : 3,
    'TH' : 4,
    'F' : 5,
    'SA' : 6,
    'SU' : 7
}

function get_date(task) {
    start_time = task.start_time.split(":");
    end_time = task.end_time.split(":");

    var start_date = new Date(0, 0, day_to_number[task.start_day], start_time[0], start_time[1], 0)
    var end_date = new Date(0, 0, day_to_number[task.end_day], end_time[0], end_time[1], 0)

    return (start_date, end_date)
}

$( document ).ready(function() {
    for (i = 0; i < schedule_list.length; i++) {
        // TODO: validate date
    }
});