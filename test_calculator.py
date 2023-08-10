
import pytest
from calculating import Calculator


def test_is_valid():
    
    '''This function tests the Calculator's is_valid() and _calculate() methods with digits, (weird) characters and etc. 
    to make sure that if someone tries to put something like that into the expression, it won't actually go through '''
    pythonCalculator = Calculator()
    
    assert pythonCalculator.is_valid('2-2-5') == True
    assert pythonCalculator.is_valid('2-2') == True
    assert pythonCalculator.is_valid('999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999-999999999999999999999999999999999999999999999999999999999999999999999999999') == True
    assert pythonCalculator.is_valid('2*(3+5)') == True
  
    assert pythonCalculator._calculate(2,2,'+') == 4  
    assert pythonCalculator._calculate(5,3,'-') == 2
    assert pythonCalculator._calculate(6,6,'*') == 36
    assert pythonCalculator._calculate(6,2,'/') == 3  
    
    assert pythonCalculator.is_valid('(6+6)') == True 
    assert pythonCalculator.is_valid('3+5)') == False  # Fixed
    assert pythonCalculator.is_valid('(6+3') == False 
    assert pythonCalculator.is_valid("!@#$%^&*()_/**-+]=,.;/") == False #Fixed     

    with pytest.raises(TypeError):
        pythonCalculator.is_valid('🍮🍮🍮🍮🍮🍮🍮🍮  Δⓓ;ㄥ𝕤נ𝒇𝕘нנ𝐨𝔼ฬⓇυเʳｕˣ.ᑕνᵐ ;ⓧＣ𝕃𝓴;đғ𝓸;∂ŜｆҜ;Ŝ𝒹ℱĻк𝕊Ⓓ;ᖴｌＫ𝓼Đ;Ｆк  🎯🎄') 
        pythonCalculator._calculate('🍮','🍮','/')

    with pytest.raises(TypeError):
        pythonCalculator.is_valid("شسزذدسيپويريل؛سدلفكسد؛لفكچ.،ڢمخ.،ڢمخ.ڢم؛اسدك؛اسلدكد") 
        pythonCalculator._calculate('دل','دل','/')

    with pytest.raises(TypeError):
        pythonCalculator.is_valid("a̵̧̖͎̟̣̲͔̩͈͕͇͙̱̪̯̥͇̙͇͎̜͙̱͙̠̣̭͈͒̈́̔̂̈́̐͛̀͗̀̌̓̊̌́͌͋́̀͜͝͝͝d̶͖͎̻̀̀̽̑͌̍̏̅͗̚;̷̢̡̧͇͇̤͓͚͓͕̪̺̤̪̱͖͇̲̗̻̺̩̼͗͋̏̀̓̄̽̂͆͌͝l̶̨̩̯̣͕̩̳̯͕̳̥̐͛͗͆͊̿̐̒̄̃̓̓̀̅͊͐́̚̕̕͝s̵̤͍̤̪͈͖̙͕̠̥̭͓͆̈́̅̒̀̽̐̃͌̇̐́͊̊̑̿̅̂̄̈̆̇̚͝j̵̡̡̟̞͍̰̺̯̃̿͊̅̀͋̆̒̔̽͊̋̿̐̌͜ͅf̸̨̢̬̠̙͒͐͌̅͗͒̉̽͑͛̉͐͂͑̀́͛̋͒͋̔̕̚̕͝ͅg̷̢̭̺̞̘̟̰̱̲̜̦̽̉͊͊͋̆̅͐̅͑͊͂͗̅̓̈́̒͛̍̒̀͘͠ḩ̴͙̯̥̠̩̘̙̥̮̩̰̙̺̦̗̿̓̉͛͐̿̄̾̂͒̇̊̃̍͌̄́̕͘͝͝ͅͅj̸̢̜̤͖̻̹̹̩̣͚̺̘̖͎̯͈̎͆̉̃͛̓̐̓̾́̔̽̔̎̈̊̑̀͛̓͂̀̚̚͜͠ö̴͇̦̯͈͎̠͕̞͕͖͖̘͓̣̦̪͔̬̳̹͍̹̩̻̺͛̇̓ͅȩ̶͙̣̖̪͔͎͉͇̲̓̆̃̽́͐ͅw̷̗̲̒͗̂͑̍́͗̔͐̕͠r̷̘͐̎͌͆͗͛̿͒̈́͐̀ṳ̸̹̘͉̼̱̪̪̺͖̭͈͖̝̙͕̤̳̻̿̓͐͛́̏͆̈́͂͂̀͗̏͐̀̐̀̎͋͂̔̂͜͝ǐ̸̛͔̉́͌̉͂́̒̾̐́͊͐͒͗͐̿̾͐̇̓̔̚̕͘̚͠ȓ̴̛͉͈̞̰̼̦͖͖̇̀̊̃͊̌̇̂ͅủ̸̬̇́͗͊͌̾̍̒̈́̇̋͗̐̂͘̕x̷͇͍̳̱̩̘͇͆̌̑̊̔̓̒̒͂̈́̓̔̋͝͝ͅ.̵̯͙̋̽̊̏̊c̶̡̧̣̜̞̣̪̙̱̓͒̓͗̓͋͐̿̈́͆̂͜͝v̸̨̧̨͉͍͓͔̯͆̊̆̌͐̏m̶̧͕̺̞̻̰͓̬̤̣̺͚͎̝͕̜̮̪̮̥̮͉̺̼̭͗͆̀̂̽̽̔̄͛̊̓͑̇̅̃̈́̍͗̌͊̇͑̕͘͜͜͝͝͝ ̵̛̛̲̦̻͖̟͚̗̱̥̗̜̓̽̓̓̑̊̽͆̆͑̀̾̔̆̽̍̈́̽̐̑̕͘;̸̨̛̠̰̳̬̺̮̺͎͜x̷̘̑͛̿̇̈́̌̿̑̀ç̴̼̖̪̙̩̍́̆l̷̩̺͍̠̻̯͎̱̀̉́͗̿͌̉̈́̿̇̚͜͝ͅķ̵̢̛͍͔͈̤̺͓͈̪̫̤͕͉̱̺̰́̈́͆͗̊͊͛͌͑͊͗̂͗̒͑̔͑͛̇͌͌̃̅͌͝͝;̸̨̨̫̗̮̞̬͔̯̲̦̥̥̹̺̙̪̦͎̓̅͂̓͂̋͜͝d̸̩͖͎̼̺̂̈́͊̉̾͑̽͌̓f̸̢̧̨̧̗̬̦̠̮̞̰̯̬̲̗̯̭̲̗̼͇̟̱̺̱̱̦̠̿̔́̃͑̓͋̽͌̈́͆͊̍̌̌́̈́̽̆̄̾̌͐̂̔̇̏̕͝ͅǫ̷͕̩̱̭̠͓̻͈̠̙̽͆̎̊̈́͑̇̓̓́͊͊͑̒̇̍̊̚̕̚͘͜͜͜͝͝͝;̷̭̋͋͋͂̑̇́̆̀̓̇̂̌̄̀͑͆̀̐̆̀͛͐͛̏̌̽͠͠ḑ̶̮͖̬͓̪̟͇̙̰̓́̄̈́̈ş̵̭̪͙͎̳̩̟̠̯̲̻̖̮͕̖͚̤͚̪̆͌̓͌̃̈́̌̀́͐͒̑̎͗͘͜ḟ̵̧̨̧̛̞͕̘̪͙͎̊̐̄́̀̈́̏̏̏̐͑̔͋́̾̐͐̾̿̑̄͆̓̈̇͜͝͝ͅk̶̡̡̢̪̭̗͇̤̗̭̞̗͍̺̟͇̫͉̰̝̺̊͆̌̅̔̃̍̎̐̇̒̑͋̆͆̓̿̆̐̇̅͒͒͌̋͘͘͘͜͠͝;̴̢̡͇̪̞̜̟͓̩̻̬̲̲̘͓̼̥͇̦̫̲̼̌͂͗͛̓̍̐̈́̕͜s̷̡̛͙̠̻͚͓̯̹̠̤͔͕͚̬̞̺̟̪͙̭̟̩̈̎̀͒̿̂̾̉́͐͗͒̄̽̿̏̊̋̉̏͜͝͝͝͝d̵̡̢̡̢͙̦̟̘̙̦͎̙̱͉̠͎̣̗̗̺͎͉̯̤͈̖͊͋̈̆̇͋̃́͛͆̅̀̉̊͘͠͝ͅͅf̸̨̤͍͖̲͍̗̩̬̫̙̺̓̅͛́̐̌̿̈͠͝l̶̡̟̥̜͎̱̽̋́͒̆̓̿̈͂͂̌̈́̉̈̋͛̓̂̽̕k̴̨̢̢̹͖̩͉͍̮̹̞̔́̑͊̇͂̄͆̈́̿̓̓́̾͌̂̉̈́̇̉̉̀͗̎̌͑͒̏͝͝s̸̢̨̛̫̖͔̞̹̯̻̟̠̞̹̺̤̉̈́̔̂̌͌̒͂͛̓̈́̓͌͗͘͝͝d̸̨̢̧̡̛͚̱̯̮͖̳̻͓̗̩̂͐͆͛̉̿́̑̃̾̉̅̓̿͂͂̓͌̓̿͋͑̽̾̈͘͘͠͝ͅ;̴̧̢̢̢̛̦̤̣͎͉͔̠̠͔̲͙͖͈̝̣̺̱̤͔̒̀̊̽̓̾̃̀̽͛f̵̭̟͓̝͎̔̃͗͗̃̓̒͒̈́͑͑̊͋̐͂͊̃̊̈́̈̓̋̏̕̚͜͜͝͝ļ̷̩̖̭͍͇̜̙͕̼̯͔̯̮̮̭̜̈͌̊͑͋̋͛̔̚͘͠k̷̨̢̛̝̙̫̹̱͈̟̥͕̰̼̼̲͈̝̗̳̞̺͈̀́̐͂͋̀͒͋̈͆̾͐́̐s̴̢͔̥̺͙̖̿́̅͘̕ḑ̶̨̛̮̯̪̭̰̤̞̣̻̩̱̂͑͋̓̓̈́̇͂̈́͑̓̈̒̔̂̈́̏̕̚͘͠͠;̷̧̱̗̮̗̥̯̜͙̣̟͓͚̲͓̹̫̠̤̻̬̔͆̾̄͌͑̊̆͂̑͋͋̓͆̎͌̀͆̀̓̿̚͘̚͘͠͠͠ͅf̶̛̠̣͚̳͖͚̈̉͌͐͑̀͛͑̿͝͝͝k̷̨̡̢̛͔̰̗͉̺͚̳͓̺̹͙̈́̐̃̽̈́́̒̈̒͆̽̿͌̈́̓̈̄̾̚")
        pythonCalculator._calculate("d̶͖͎̻̀̀̽̑͌̍̏̅͗̚;̷̢̡̧͇͇̤͓͚͓͕̪̺̤̪̱͖͇̲̗̻̺̩̼͗͋̏̀̓̄̽̂͆͌͝l̶̨̩̯̣͕̩̳̯͕̳̥̐͛͗͆͊̿̐̒̄̃̓̓̀̅͊͐́̚̕̕͝s̵̤͍̤̪͈͖̙͕̠̥̭͓͆̈́̅̒̀̽̐̃͌̇̐́͊̊̑̿̅̂̄̈̆̇̚͝",'d̶͖͎̻̀̀̽̑͌̍̏̅͗̚;̷̢̡̧͇͇̤͓͚͓͕̪̺̤̪̱͖͇̲̗̻̺̩̼͗͋̏̀̓̄̽̂͆͌͝l̶̨̩̯̣͕̩̳̯͕̳̥̐͛͗͆͊̿̐̒̄̃̓̓̀̅͊͐́̚̕̕͝s̵̤͍̤̪͈͖̙͕̠̥̭͓͆̈́̅̒̀̽̐̃͌̇̐́͊̊̑̿̅̂̄̈̆̇̚͝','d̶͖͎̻̀̀̽̑͌̍̏̅͗̚;̷̢̡̧͇͇̤͓͚͓͕̪̺̤̪̱͖͇̲̗̻̺̩̼͗͋̏̀̓̄̽̂͆͌͝l̶̨̩̯̣͕̩̳̯͕̳̥̐͛͗͆͊̿̐̒̄̃̓̓̀̅͊͐́̚̕̕͝s̵̤͍̤̪͈͖̙͕̠̥̭͓͆̈́̅̒̀̽̐̃͌̇̐́͊̊̑̿̅̂̄̈̆̇̚͝')
        
    with pytest.raises(TypeError):
        pythonCalculator.is_valid('print("Hello World")')
        pythonCalculator._calculate('p', 'g', '')

    with pytest.raises(ZeroDivisionError):
        pythonCalculator._calculate(3,0,'/')

    with pytest.raises(ZeroDivisionError):
        pythonCalculator.is_valid('3/0')

# Failed tests that fail since the calculator class cannot raise Exceptions 
@pytest.mark.xfail
def test_is_not_valid():
    pass    




    



    
