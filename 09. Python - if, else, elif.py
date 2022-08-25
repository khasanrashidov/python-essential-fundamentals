## if <condition>:
##     <instruction>
##     <instruction>
##     ...

print('='*30)
print()
traffic_light=True

if traffic_light==True:
    print('Attention! Traffic lights!')
print('\nFollow the traffic rules!')
print('='*30)
print()

## or
## because, by default,
## the value of traffic_light is True

if traffic_light: 
    print('Attention! Traffic lights!')
print('\nFollow the traffic rules!')
print('='*30)

## when traffic_light is False

traffic_light=0

if traffic_light: ## dead code
    print('Attention! Traffic lights!')
print('\nFollow the traffic rules!')
print('='*30)
print()

## or using 'else:'
##
## if <condition>:
##     <instruction>
##     <instruction>
##     ...
## else:
##     <instruction>
##     <instruction>
##     ...

traffic_light=0

if traffic_light: 
    print('Attention! Traffic lights!')
else:
    print('There are no traffic lights')
print('\nFollow the traffic rules!')
print('='*30)
print()

## if <condition>:
##     <instruction>
##     <instruction>
##     ...
## elif <condition>:
##     <instruction>
##     <instruction>
##     ...
## elif <condition>:
##     <instruction>
##     <instruction>
##     ...
## else:
##     <instruction>
##     <instruction>
##     ...

traffic_light=1

##signal = 'red'
##signal = 'yellow'
##signal = 'green'
signal = ''

if traffic_light: 
    print('Attention! Traffic lights!\n')
    if signal == 'red':
        print('Red. \nStop!')
    elif signal == 'yellow':
        print('Yellow. \nWait...')
    elif signal == 'green':
        print('Green, \nDrive!')
    else:
        print('Traffic lights are not working')
else:
    print('There are no traffic lights')
print('\nFollow the traffic rules!')
print('='*30)
print()
