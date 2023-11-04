n = int(input())
vacancies_competition = dict()
for i in range(n):
    s, m = input().split(',')
    vacancies_competition[s] = [int(m), ]

k = int(input())
for i in range(k):
    candidate_id, vac_name, solved, fine = input().split(',')
    a = candidate_id, int(solved), int(fine)
    vacancies_competition[vac_name].append(a)

answer = []

for vac_name in vacancies_competition:
    n = len(vacancies_competition[vac_name]) - 1
    if n > vacancies_competition[vac_name][0]:
        vacancies_competition[vac_name][1:] = sorted(vacancies_competition[vac_name][1:],
                                                     key=lambda x: x[1], reverse=True)
        i = 0
        tasks = 6
        while i < vacancies_competition[vac_name][0]:
            if vacancies_competition[vac_name][i+1][1] == tasks:
                i += 1
            else:
                tasks -= 1
        while True:
            if i+1 > n or vacancies_competition[vac_name][i+1][1] != tasks:
                break
            i += 1
        vacancies_competition[vac_name] = sorted(vacancies_competition[vac_name][1:i+1],
                                                 key=lambda x: (x[1], -x[2]), reverse=True)[:vacancies_competition[vac_name][0]]
        answer.extend(list(map(lambda x: x[0], vacancies_competition[vac_name])))
    else:
        answer.extend(list(map(lambda x: x[0], vacancies_competition[vac_name][1:])))


# рабочий вариант, но долго сортируется весь список проверить что быстрее
for vac_name in vacancies_competition:
    vacancies_competition[vac_name][1:] = sorted(vacancies_competition[vac_name][1:], key=lambda x: (x[1], -x[2]), reverse=True)
    answer.extend(list(map(lambda x: x[0], vacancies_competition[vac_name][1: vacancies_competition[vac_name][0] + 1])))

answer.sort()
for name in answer:
    print(name)
