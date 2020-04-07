import os
class conf():
    #where shared variables are
    token= os.environ['TOKEN'] #replace os.environ['TOKEN'] with your token
    prefix1='ap_'
    prefix2='Ap_'
    name='Arnold Palmer'
    cogd='Cogs'
    type_speed=1
    playing_msg=[f"Type 'ap_help' for help!", "Golf", 'Mario Golf', 'Let\'s Golf', 'Golf With Friends', 'Golf It', '', 'Tiger Wood\'s PGA Tour \'14', 'World Golf Tour', 'Golf Story', 'Everybody\'s Golf']
    w_tog_on = []
    color = 0xfedc01
    triggers =[]
    everyone_tag = "Nice try, no ping for you"
    #colors (stolen from dokis)
    err = 0xC91313 # The Error Embed Colour
    norm = 0xdb7915 # The Normal or Yeah sure i did this command heres an embed color, Embed Colour
    warn = 0xff42e2 # The Warning Embed Colour
    suc = 0xff42e2 # The Success (i did a thing) Embed Colour
    
