short_hair = input('Собака короткошерстной породы? ')
if short_hair == 'да':
   height50 = input('Рост собаки менее 50 см? ')
   if height50 == 'да':
      tail = input('У собаки короткий хвост? ')
      if tail == 'да':
          print('Английский бульдог')
      else:
          long_ears = input('У собаки длинные уши? ')
          if long_ears == "да":
              print("Гончая")
          else:
              body = input('У собаки короткое тело? ')
              if body == 'Да':
                 print('Мопс')
              else:
                 print('Чихуахуа')
   else:
       weight = input('Собака весит более 50 кг? ')
       if weight == 'Да':
          print('Датский дог')
       else:
          print('Фоксхаунд')
else:
    height50 = input('Рост собаки менее 50 см? ')
    if height50 == 'Да':
       character = input('У собаки доброжелательный характер? ')
       if character == 'Да':
          print('Кокер-спаниэль')
       else:
          print('Ирландский сеттер')
    else:
        height70 = input('Рост собаки менее 70 см? ')
        if height70 == 'Да':
           long_ears = input('У собаки длинные уши? ')
           if long_ears == 'Да':
              print('Большой вандейский грифон')
           else:
              print('Колли')
        else:
            red_color = input('Окрас рыжий с белыми отметинами? ')
            if red_color == 'Да':
               print('Сенбернар')
            else:
               white_color = input('Белоснежный окрас? ')
               if white_color == 'Да':
                  print('Ирландский волкодав')
               else:
                  print('Ньюфаундленд')