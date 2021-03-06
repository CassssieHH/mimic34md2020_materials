qat = {'kind': 'AT',
  'question': 'Which of these researches primarily did medical research?',
  'tags': 'a, 1',
  'answers': {0: {'answer': 'Homer Warner',
    'feedback': 'HELP, Iliad, Bayesian diagnosis',
    'status': 'T'},
   1: {'answer': 'Benjamin Franklin',
    'feedback': 'Electricity',
    'status': 'F'},
   2: {'answer': 'Larry Weed', 'feedback': 'SOAP', 'status': 'T'},
   3: {'answer': 'James Clerk Maxwell',
    'feedback': 'Mathematical physics',
    'status': 'F'}}}
mcq = {'kind': 'MC',
  'question': 'Who was the first president of the United States',
  'tags': 'a,1',
  'correct_answer': 0,
  'answers': {0: {'answer': 'George Washington', 'feedback': 'Indeed!'},
   1: {'answer': 'Abraham Lincoln', 'feedback': 'Civil War'},
   2: {'answer': 'John Adams', 'feedback': 'No. 2'},
   3: {'answer': 'Benjamin Franklin', 'feedback': 'Never was'}}}

questions = [{'kind': 'TF',
  'question': 'This is not the end',
  'tags': 'a, 1',
  'correct_answer': 'T',
  'fb': {'T': 'thankfully', 'F': ''}},
 {'kind': 'MC',
  'question': 'Who was the first president of the United States',
  'tags': 'a,1',
  'correct_answer': 0,
  'answers': {0: {'answer': 'George Washington', 'feedback': 'Indeed!'},
   1: {'answer': 'Abraham Lincoln', 'feedback': 'Civil War'},
   2: {'answer': 'John Adams', 'feedback': 'No. 2'},
   3: {'answer': 'Benjamin Franklin', 'feedback': 'Never was'}}},
 {'kind': 'AT',
  'question': 'Which of these researches primarily did medical research?',
  'tags': 'a, 1',
  'answers': {0: {'answer': 'Homer Warn',
    'feedback': 'HELP, Iliad, Bayesian diagnosis',
    'status': 'T'},
   1: {'answer': 'Benjamin Franklin',
    'feedback': 'Electricity',
    'status': 'F'},
   2: {'answer': 'Larry Weed', 'feedback': 'SOAP', 'status': 'T'},
   3: {'answer': 'James Clerk Maxwell',
    'feedback': 'Mathematical physics',
    'status': 'T'}}},
 {'kind': 'FR',
  'question': 'I am lonely',
  'tags': 'a, 1',
  'feedback': 'I am too'},
 {'kind': 'TF',
  'question': 'This is nit the end',
  'tags': 'a,1',
  'correct_answer': 'T',
  'feedback': {'T': 'Thankfully', 'F': 'Pessimist'}}]
