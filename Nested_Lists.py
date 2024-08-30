if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
       
        name = input()
        score = float(input())
        
        students.append([name,score])

        # print(students)

    unique_score = sorted(set(score for name,score in students))

    if len(unique_score) > 1:
        second_score = unique_score[1]
        second_lowest_score = [name for name, score in students if score == second_score]

        second_lowest_score.sort()

        # Print each name on a new line
        for student in second_lowest_score:
            print(student)

