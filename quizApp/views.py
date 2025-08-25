from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, Answer, UserAttempt

@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == "POST":
        score = 0
        for question in quiz.questions.all():  # Fixed: Quiz.questions.all() -> quiz.questions.all()
            selected = request.POST.get(str(question.id))
            if selected:
                answer = Answer.objects.get(id=selected)
                if answer.is_correct:
                    score += 1
        UserAttempt.objects.create(user=request.user, quiz=quiz, score=score)
        return render(request, 'quiz_result.html', {'quiz': quiz, 'score': score})
    return render(request, 'take_quiz.html', {'quiz': quiz})  # Added questions to context

@login_required
def quiz_result(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    attempt = UserAttempt.objects.filter(user=request.user, quiz=quiz).last()
    return render(request, 'quiz_result.html', {'quiz': quiz, 'score': attempt.score if attempt else None})

# Create your views here.