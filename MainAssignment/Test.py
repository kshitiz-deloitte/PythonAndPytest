import re


def get_hr_and_min(given_time):
    given_time = given_time.split(" ")
    cal_hr, cal_min = int(re.findall(r'\d+', given_time[0])[0]), int(re.findall(r'\d+', given_time[1])[0])
    return cal_hr, cal_min


def cal_movie_timing():
    movie_length_hr, movie_length_min = get_hr_and_min("1hr 30min")
    movie_number = 4
    movie_first_show_hr, movie_first_show_min = get_hr_and_min("8hr 30min")
    movie_interval_hr, movie_interval_min = get_hr_and_min("1hr 15min")
    movie_gap_hr, movie_gap_min = get_hr_and_min("0hr 15min")
    total_run_time_min = movie_length_min + movie_interval_min
    min_to_hr = total_run_time_min // 60
    remaining_min = total_run_time_min % 60
    total_hr = movie_length_hr + movie_interval_hr + min_to_hr
    print(remaining_min, total_hr, movie_gap_min)

    start_hr = 0
    start_min = 0
    for i in range(movie_number):
        if i == 0:
            start_hr = movie_first_show_hr
            start_min = movie_first_show_min
        end_min = remaining_min+start_min
        end_min_to_hr = end_min // 60
        end_remaining_min = end_min % 60
        end_hr = start_hr + end_min_to_hr + total_hr
        yield f"{start_hr}:{start_min}-{end_hr}:{end_remaining_min}"
        next_min = end_remaining_min + movie_gap_min
        next_min_to_hr = next_min // 60
        next_remaining_min = next_min % 60
        start_hr = end_hr + movie_gap_hr + next_min_to_hr
        start_min = next_remaining_min

print(list(cal_movie_timing()))
