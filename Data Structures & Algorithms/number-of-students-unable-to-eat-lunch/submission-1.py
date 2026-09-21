class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while True:
            all_students_hungry = True

            for i, s in enumerate(students):
                if sandwiches[0] == s:
                    sandwiches.pop(0)
                    students.pop(i)
                    all_students_hungry = False

            if all_students_hungry:
                break

        return len(sandwiches)            

                
                


