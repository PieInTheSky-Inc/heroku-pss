import discord
import subprocess

def shell_cmd(cmd):
    result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')
    
def get_user_pss_toolkit():
    return discord.Client.get_user(id: 487398795756437514)
