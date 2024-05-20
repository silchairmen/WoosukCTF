# $Id: local.rules,v 1.11 2004/07/23 20:15:44 bmc Exp $
# ----------------
# LOCAL RULES
# ----------------
# This file intentionally does not come with signatures.  Put your local
# additions here.
# welcome to soti
alert tcp any any -> any 10001 (msg:"welcome to soti flag"; content:"index.php"; nocase; sid:1000001; rev:1; logto:"/var/log/snort/welcomeToSoti.log";)

# Murder help
alert tcp any any -> any 10002 (msg:"murder help flag"; content:"{{"; pcre:"/\{\{.*?(fl|fla|flag).*?\}\}/i"; sid:1000002; rev:1; logto:"/var/log/snort/murd>

# restricted globbing
alert tcp any any -> any 10003 (msg:"restricted globbing flag"; content:"http://jalnik.vercel.app/introduce"; content:"http@0/"; sid:1000003; rev:1; logto:>

# The Cookie_I_Made
alert tcp any any -> any 10004 (msg:"The Cookie I Made"; uricontent:"/admin"; nocase; content:"../flag.txt"; sid:1000004; rev:1; logto:"/var/log/snort/theC>

# do you know proxy?
alert tcp any any -> any 10005 (msg:"do_you_know_proxy? flag"; content:"YWRtaW4="; sid:1000005; rev:1; logto:"/var/log/snort/doYouKnowProxy.log";)

# show me the money
alert tcp $HOME_NET 10006 -> $EXTERNAL_NET any (msg:"show_me_the_money flag"; content:"The flag is:"; sid:1000006; rev:1; logto:"/var/log/snort/showMeTheMo>

# unauthorized_access
alert tcp $HOME_NET 10007 -> $EXTERNAL_NET any (msg:"unauthorized_access flag"; content:"Flag:"; sid:1000007; rev:1; logto:"/var/log/snort/unauthorized_acc>

# Crack_the_egg
alert tcp any any -> any 10008 (msg:"Crack_the_egg flag"; uricontent:"/egg1449.png"; sid:1000008; rev:1; logto:"/var/log/snort/crackTheEgg.log";)