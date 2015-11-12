
day_to_number = {
    'M' : 1,
    'TU' : 2,
    'W' : 3,
    'TH' : 4,
    'F' : 5,
    'SA' : 6,
    'SU' : 7
}

schedule = [];

$( document ).ready(function() {
    for (i = 0; i < schedule_list.length; i++) {
        schedule.push(get_dates(schedule_list[i]));
    }
});

function get_dates(task) {
    start_time = task.start_time.split(":");
    end_time = task.end_time.split(":");

    var start_date = new Date(0, 0, day_to_number[task.start_day], start_time[0], start_time[1], 0);
    var end_date = new Date(0, 0, day_to_number[task.end_day], end_time[0], end_time[1], 0);

    return { start_date : start_date, end_date: end_date };
}

function is_task_within_another(t, a) {
    return (a.start_date < t.start_date && a.end_date > t.start_date) ||
        (a.start_date < t.end_date && a.end_date > t.end_date);
}

function is_task_within_another_in_schedule(task) {
    for (i = 0; i < schedule.length; i++) {
        if (is_task_within_another(task, schedule[i])) {
            return true;
        }
    }
    return false;
}

function validate() {
    var candidate = get_dates({
        start_day : $( "#id_start_day" ).val(),
        start_time : $( "#id_start_time" ).val(),
        end_day : $( "#id_end_day" ).val(),
        end_time : $( "#id_end_time" ).val() });

    if (is_task_within_another_in_schedule(candidate)) {
        alert("Cannot add: rule is within another existing!");
        return false;
    }
    return true;
};