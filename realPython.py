#Handle Missing Dictionary Keys With collections.defaultdict()
# grades = [
#     ('elliot', 91),
#     ('neelam', 98),
#     ('bianca', 81),
#     ('elliot', 88),
# ]
#
# from collections import defaultdict
# student_grades = defaultdict(list)
# for name, grade in grades:
#     student_grades[name].append(grade)
# print(student_grades)

#Count Hashable Objects With collections.Counter
# from collections import Counter
# words = "if there was there was but if \
# there was not there was not".split()
# counts = Counter(words)
# print(counts.most_common(1))

#
# a={'4':'3','2':'1','5':'3','0':'1'}
# r=sorted(a.items(),key=lambda x:x[0])
# print(r)
# a,b,c=1,1,1
# if a==1 or b==1 or c==1:
#     print('true')
# if a or b or c:
#     print('t')
# if any((a,b,c)):
#     print('tr')
# if 1 in (a,b,c):
#     print('tru')

# name_for_userid = {
#     382: "Alice",
#     590: "Bob",
#     951: "Dilbert",
# }
#
# def nameGetter(name):
#     return 'hi %s!'%name_for_userid.get(name,'there')
#
# print(nameGetter(5920))