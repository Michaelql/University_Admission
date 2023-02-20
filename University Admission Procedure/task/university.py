def get_one_subject(subject, rank):
    rank_list = [i for i in student_score_list if i[7 + rank] == subject]
    sort_list(rank_list, subject)
    return rank_list


def out_print(list_of_print, subject, num_of_print):
    sort_list(list_of_print, subject)
    exam_select = dic_score_subject.get(subject)
    file_out = open(f'{subject}.txt', 'w')
    for i in range(0, num_of_print):
        if i >= len(list_of_print):
            break
        if subject in list_of_print[i]:
            score = float(list_of_print[i][2 + exam_select[0]]) + float(list_of_print[i][2 + exam_select[1]])
            score /= 2
            special = float(list_of_print[i][6])
            final_score = max(score, special)
            txt_print = list_of_print[i][0] + ' ' + list_of_print[i][1] + ' ' + str(final_score) + '\n'
            file_out.write(txt_print)
    file_out.close()


def sort_list(origin_list, subject):
    exam_select = dic_score_subject.get(subject)
    origin_list.sort(key=lambda x: (-max((float(x[2 + exam_select[0]]) + float(x[2 + exam_select[1]])) / 2,
                                         float(x[6])), x[0], x[1]))


file = open('applicants.txt')
every_sub_num = int(input())
student_score_list = [i.split() for i in file]
subject_score_list = [[], [], [], [], []]  # store 5 subjects' students
subjects = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
dic_score_subject = {'Biotech': (0, 1), 'Chemistry': (1, 1),
                     'Engineering': (2, 3), 'Mathematics': (2, 2), 'Physics': (0, 2)}
for option in range(0, 3):
    for i in range(0, 5):
        subj = subjects[i]
        one_subject_list = get_one_subject(subj, option)
        for j in one_subject_list:
            if len(subject_score_list[i]) < every_sub_num:
                subject_score_list[i].append(j)
                student_score_list.remove(j)
for i in range(0, 5):
    out_print(subject_score_list[i], subjects[i], every_sub_num)
file.close()

