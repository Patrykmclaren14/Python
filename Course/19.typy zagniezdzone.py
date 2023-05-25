Listagosci1 = {
                    ('Patryk', 17, 'mężczyzna'),
                    ('Kuba', 24, 'mężczyzna'),
                    ('Olek', 12, 'mężczyzna')
               }

print(Listagosci1)

listagosci2 = {
    ('Patryk', 17, 'mężczyzna'),
    ('Damian', 43, 'mężczyzna')
               }


print(listagosci2 | Listagosci1)
                 
print(Listagosci1[1][2]) #gdy zmienna jest lista