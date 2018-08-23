from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
import paramiko
import six
from ..models import ServerDetail

def ssh(ipaddress,user,key, command):
    try:
        ssh = paramiko.SSHClient()
        pkey = paramiko.RSAKey.from_private_key(six.StringIO(key))
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ipaddress, username=user, pkey=pkey)
        stdin, stdout, stderr = ssh.exec_command(command)
        command_output=stdout.readlines()
        command_error=stderr.readlines()
        ssh.close()
        return command_output,command_error
    except:
        content={"status": "Authentication Failed"}
        return Response(content)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def os_view(request, ipaddress, format=None):
    ip_list = list(ServerDetail.objects.filter(user=request.user).values("ipaddress"))
    ip_list=[ip['ipaddress'] for ip in ip_list]
    if ipaddress in ip_list:
        data=list(ServerDetail.objects.filter(ipaddress=ipaddress).values("sshKey","server_user"))[0]
    output,error=ssh(ipaddress=ipaddress,key=data['sshKey'],user=data['server_user'],command="lscpu")
    output=[item.split(":") for item in output]                    
    output={ k[0]: k[1].strip().replace("\n","") for k in output }  
    content = {
        "output": output, 
        "error" : error
    }
    return Response(content)
