from django.shortcuts import render
 
# Create your views here.
#from .detect_drowsiness import develop


def myview(request):
    #develop()
    return render(request,'view.html',{})

import subprocess

def detect(request):
    subprocess.run(['python', 'destroy.py'], shell=False)
    pk=subprocess.Popen(['python', 'detect_drowsiness.py'], shell=True)
    #pk=subprocess.run(['python', 'destroy.py'], shell=True)

    return render(request,'view.html',{})
    '''if request.method == 'GET':qq
    form = your_form_name() 
  else:
    if form.is_valid():
      info = request.POST['info_name']
      output = script_function(info) 
      // Here you are calling script_function, 
      // passing the POST data for 'info' to it;
      return render(request, 'your_app/your_template.html', {
        'info': info,
        'output': output,
      })
  return render(request, 'your_app/your_template.html', {
    'form': form,
    })


def script_function()
  print post_from_form //optional,check what the function received from the submit;
  return subprocess.check_call(['/path/to/your/script.py', post_from_form])
'''