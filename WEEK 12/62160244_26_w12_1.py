from fysom import Fysom
finit_state = Fysom({ 'initial': 's0','events': [
    {'name': '0', 'src': 's0', 'dst': 's1'},
    {'name': '0', 'src': 's1', 'dst': 's3'},
    {'name': '0', 'src': 's2', 'dst': 's2'},
    {'name': '0', 'src': 's3', 'dst': 's3'},
    {'name': '1', 'src': 's0', 'dst': 's1'},
    {'name': '1', 'src': 's1', 'dst': 's2'},
    {'name': '1', 'src': 's2', 'dst': 's3'},
    {'name': '1', 'src': 's3', 'dst': 's1'}]})
number = int(input('number of Input = '))
print('Start state',finit_state.current)
for i in range(number):
    name = input('Enter your input : ')
    str_name = str(name)
    if str_name == '0' and finit_state.isstate('s0'):
        finit_state.trigger(str_name)
        print('State',finit_state.current)
        print("=" * 30)
    elif str_name == '0' and finit_state.isstate('s1'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("=" * 30)
    elif str_name == '0' and finit_state.isstate('s2'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("=" * 30)
    elif str_name == '0' and finit_state.isstate('s3'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("=" * 30)
    elif str_name == '0' and finit_state.isstate('s4'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("=" * 30)
    elif str_name == '1' and finit_state.isstate('s0'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("=" * 30)
    elif str_name == '1' and finit_state.isstate('s1'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("=" * 30)
    elif str_name == '1' and finit_state.isstate('s2'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("=" * 30)
    elif str_name == '1' and finit_state.isstate('s3'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("=" * 30)
    elif str_name == '1' and finit_state.isstate('s4'):
        finit_state.trigger(str_name)
        print('State', finit_state.current)
        print("="*30)
    else:
        print('ERROR')
        print("=" * 30)
        break
print("Stop at state : ",finit_state.current)