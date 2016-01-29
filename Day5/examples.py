from data_structure import PhoneBookList

b = PhoneBookList()
b.add_contact('kate', '883993')
b.add_contact('maggie', '883993')
b.add_contact('james', '883993')

print b.book

print b.search('kate')
print b.search('maggie')
print b.search('jane')

b = PhoneBookDict()
b.add_contact('kate', '883993')
b.add_contact('maggie', '883993')
b.add_contact('james', '883993')

print b.book

print b.search('kate')
print b.search('maggie')
print b.search('jane')