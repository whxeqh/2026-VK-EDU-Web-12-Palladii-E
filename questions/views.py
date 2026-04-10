from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def get_popular_tags():
    return ['python', 'django', 'mysql', 'perl', 'javascript']

def get_best_members():
    return ['Поздышев Александр', 'Опритов Артём', 'Виндман Александр']

def paginate(objects_list, request, per_page=10):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page', 1)

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page


def make_fake_questions(count=30):
    questions = []

    for i in range(1, count + 1):
        question = {
            'id': i,
            'title': 'Question #' + str(i) + ': How to do something useful?',
            'text': 'This is a detailed description of question #' + str(i) + '. Lorem ipsum dolor sit amet.',
            'tags': ['python', 'django'],
            'likes': i * 3 % 20,
            'answers': i % 7,
            'created_at': str(i) + ' hours ago',
        }
        questions.append(question)

    return questions


def make_fake_answers(count=15):
    answers = []

    for i in range(1, count + 1):
        answer = {
            'id': i,
            'text': 'Answer #' + str(i) + ': Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'likes': i * 2 % 10,
            'is_correct': (i == 1),
            'created_at': str(i) + ' hours ago',
        }
        answers.append(answer)

    return answers


def index(request):
    questions = make_fake_questions(30)
    page = paginate(questions, request, per_page=5)

    context = {
        'page_obj': page,
        'popular_tags': get_popular_tags(),
        'best_members': get_best_members(),
    }
    return render(request, 'questions/index.html', context)


def hot(request):
    questions = make_fake_questions(20)

    sorted_questions = []
    while len(questions) > 0:
        max_question = questions[0]
        for q in questions:
            if q['likes'] > max_question['likes']:
                max_question = q
        sorted_questions.append(max_question)
        questions.remove(max_question)

    page = paginate(sorted_questions, request, per_page=5)

    context = {
        'page_obj': page,
        'popular_tags': get_popular_tags(),
        'best_members': get_best_members(),
    }
    return render(request, 'questions/hot.html', context)


def tag(request, tag_name):
    all_questions = make_fake_questions(30)

    questions_with_tag = []
    for q in all_questions:
        if tag_name in q['tags']:
            questions_with_tag.append(q)

    page = paginate(questions_with_tag, request, per_page=5)

    context = {
        'page_obj': page,
        'tag': tag_name,
        'popular_tags': get_popular_tags(),
        'best_members': get_best_members(),
    }
    return render(request, 'questions/tag.html', context)


def question(request, question_id):
    all_questions = make_fake_questions(30)

    # ищем вопрос по id
    found_question = None
    for q in all_questions:
        if q['id'] == question_id:
            found_question = q
            break

    # если не нашли — берём первый
    if found_question is None:
        found_question = all_questions[0]

    answers = make_fake_answers(15)
    page = paginate(answers, request, per_page=5)

    context = {
        'question': found_question,
        'page_obj': page,
        'popular_tags': get_popular_tags(),
        'best_members': get_best_members(),
    }
    return render(request, 'questions/question.html', context)
