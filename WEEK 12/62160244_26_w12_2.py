from fysom import Fysom
finit_state = Fysom({ 'initial': 's0','events': [
    {'name': '0', 'src': 's0', 'dst': 's1'},
    {'name': '0', 'src': 's1', 'dst': 's5'},
    {'name': '0', 'src': 's2', 'dst': 's3'},
    {'name': '0', 'src': 's3', 'dst': 's0'},
    {'name': '0', 'src': 's4', 'dst': 's2'},
    {'name': '0', 'src': 's5', 'dst': 's4'},
    {'name': '1', 'src': 's0', 'dst': 's4'},
    {'name': '1', 'src': 's1', 'dst': 's1'},
    {'name': '1', 'src': 's2', 'dst': 's0'},
    {'name': '1', 'src': 's3', 'dst': 's5'},
    {'name': '1', 'src': 's4', 'dst': 's1'},
    {'name': '1', 'src': 's5', 'dst': 's2'}]})
number = int(input('number of Input = '))
print('Start state',finit_state.current)
for i in range(number):
    name = input('Enter your input : ')
    if(name =='a'):
        name='0'
    elif(name=='b'):
        name='1'
    str_name = str(name)
    if str_name == '0' and finit_state.isstate('s0'):
        finit_state.trigger(str_name)
        print('State',finit_state.current)
        print("output = 0")
        print("=" * 30)
    elif str_name == '0' and finit_state.isstate('s1'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("output = 0")
        print("=" * 30)
    elif str_name == '0' and finit_state.isstate('s2'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("output = 1")
        print("=" * 30)
    elif str_name == '0' and finit_state.isstate('s3'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("output = 1")
        print("=" * 30)
    elif str_name == '0' and finit_state.isstate('s4'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("output = 1")
        print("=" * 30)
    elif str_name == '0' and finit_state.isstate('s5'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("output = 0")
        print("=" * 30)
    elif str_name == '1' and finit_state.isstate('s0'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("output = 0")
        print("=" * 30)
    elif str_name == '1' and finit_state.isstate('s1'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("output = 1")
        print("=" * 30)
    elif str_name == '1' and finit_state.isstate('s2'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("output = 1")
        print("=" * 30)
    elif str_name == '1' and finit_state.isstate('s3'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("output = 0")
        print("=" * 30)
    elif str_name == '1' and finit_state.isstate('s4'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("output = 1")
        print("=" * 30)
    elif str_name == '1' and finit_state.isstate('s5'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("output = 1")
        print("=" * 30)
    else:
        print('ERROR')
        print("=" * 30)
        break
print("Stop at state : ",finit_state.current)