from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_text = q["question"]
    question_answer = q["correct_answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz_brain = QuizBrain()
final_score = quiz_brain.score

print("You've completed the quiz.")
print(f"Your final score was: {final_score}/{len(question_bank)}")

