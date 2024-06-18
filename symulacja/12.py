from os.path import exists
import datetime

# ALGORITHM
def fcfs(draw, processes_tab):
  process_tab_fcfs = []
  process_tab_fcfs = processes_tab.copy()
  process_queue = []
  time = 0
  waiting_time = 0
  numb_processes = len(process_tab_fcfs)
  step = 1

  visual_process_queue_fcfs = [
    [],
    [],
    [],
    [],
    [],
    ['0      ']
  ]

  while True:
    #Adding process to queue
    del_temp = []
    for i in range (0, len(process_tab_fcfs)):
      if process_tab_fcfs[i][1] == time:
        process_queue.append(process_tab_fcfs[i].copy())
        del_temp.append(i)
    del_temp.reverse()
    for idx in del_temp:
      del process_tab_fcfs[idx]

    #FCFS
    if process_queue:
      if process_queue[0][2] == 0:
        # Count process number
        process_name = '│ P00 │'
        if process_queue[0][0] + 1 < 10:
          process_name = process_name.replace('P00', f'P{process_queue[0][0] + 1} ')
        else:
          process_name = process_name.replace('P00', f'P{process_queue[0][0] + 1}')
        
        # Count end line
        end_line = 's'
        end_line = end_line.replace('s', str(time))
        while len(end_line) < 7:
          end_line += ' '
        # Add process to visual queue
        visual_process_queue_fcfs[0].append('┌─────┐')
        visual_process_queue_fcfs[1].append('│     │')
        visual_process_queue_fcfs[2].append(process_name)
        visual_process_queue_fcfs[3].append('│     │')
        visual_process_queue_fcfs[4].append('└─────┘')
        visual_process_queue_fcfs[5].append(end_line)

        #DELETE ENDED PROCESS
        del process_queue[0]

        #Draw process queue
        if draw:
          print(f'---- Step {step} - FCFS ----')
          step += 1
          for id_line in range (0,6):
            line = str(visual_process_queue_fcfs[id_line])
            for character in "[]'":
              line = line.replace(character, '')
            line = line.replace(', ', '')
            if id_line == 5 and process_queue:
              print(line[:-7])
            else:
              print(line)
        
          input("Press enter to continue")

        if process_queue:
          waiting_time += time - process_queue[0][1]
      if process_queue:
        process_queue[0][2] -= 1


    time += 1
    if not process_queue and not process_tab_fcfs:
      break

  return waiting_time/numb_processes, visual_process_queue_fcfs

def sjf(draw, processes_tab):
  process_tab_sjf = processes_tab.copy()
  process_queue = []
  time = 0
  waiting_time = 0
  numb_processes = len(process_tab_sjf)
  step = 1

  visual_process_queue_sjf = [
    [],
    [],
    [],
    [],
    [],
    ['0      ']
  ]

  while True:
    #Adding process to queue
    del_temp = []
    for i in range (0, len(process_tab_sjf)):
      if process_tab_sjf[i][1] == time:
        process_queue.append(process_tab_sjf[i].copy())
        del_temp.append(i)
    del_temp.reverse()
    for idx in del_temp:
      del process_tab_sjf[idx]

    if time == 0:
      process_queue = sorted(process_queue, key=lambda x: x[2])

    #SJF
    if process_queue:
      if process_queue[0][2] == 0:
        # Count process number
        process_name = '│ P00 │'
        if process_queue[0][0] + 1 < 10:
          process_name = process_name.replace('P00', f'P{process_queue[0][0] + 1} ')
        else:
          process_name = process_name.replace('P00', f'P{process_queue[0][0] + 1}')
        
        # Count end line
        end_line = 's'
        end_line = end_line.replace('s', str(time))
        while len(end_line) < 7:
          end_line += ' '
        # Add process to visual queue
        visual_process_queue_sjf[0].append('┌─────┐')
        visual_process_queue_sjf[1].append('│     │')
        visual_process_queue_sjf[2].append(process_name)
        visual_process_queue_sjf[3].append('│     │')
        visual_process_queue_sjf[4].append('└─────┘')
        visual_process_queue_sjf[5].append(end_line)

        #DELETE ENDED PROCESS
        del process_queue[0]

        process_queue = sorted(process_queue, key=lambda x: x[2])

        #Draw process queue
        if draw:
          print(f'---- Step {step} - SJF ----')
          step += 1
          for id_line in range (0,6):
            line = str(visual_process_queue_sjf[id_line])
            for character in "[]'":
              line = line.replace(character, '')
            line = line.replace(', ', '')
            if id_line == 5 and process_queue:
              print(line[:-7])
            else:
              print(line)
        
          input("Press enter to continue")

        if process_queue:
          waiting_time += time - process_queue[0][1]
      if process_queue:
        process_queue[0][2] -= 1

    #print(process_queue)
    time += 1
    if not process_queue and not process_tab_sjf:
      break

  return waiting_time/numb_processes, visual_process_queue_sjf

def sjf_prio(draw, processes_tab, priority_time):
  process_tab_sjf_prio = processes_tab.copy()
  process_queue = []
  time = 0
  waiting_time = 0
  numb_processes = len(process_tab_sjf_prio)
  step = 1

  visual_process_queue_sjf_prio = [
    [],
    [],
    [],
    [],
    [],
    ['0      ']
  ]

  while True:
    #Adding process to queue
    del_temp = []
    for i in range (0, len(process_tab_sjf_prio)):
      if process_tab_sjf_prio[i][1] == time:
        process_queue.append(process_tab_sjf_prio[i].copy())
        del_temp.append(i)
    del_temp.reverse()
    for idx in del_temp:
      del process_tab_sjf_prio[idx]

    if time == 0:
      process_queue = sorted(process_queue, key=lambda x: (x[3], x[2]))
    #SJF
    if process_queue:
      if process_queue[0][2] == 0:
        # Count process number
        process_name = '│ P00 │'
        if process_queue[0][0] + 1 < 10:
          process_name = process_name.replace('P00', f'P{process_queue[0][0] + 1} ')
        else:
          process_name = process_name.replace('P00', f'P{process_queue[0][0] + 1}')
        
        # Count end line
        end_line = 's'
        end_line = end_line.replace('s', str(time))
        while len(end_line) < 7:
          end_line += ' '
        # Add process to visual queue
        visual_process_queue_sjf_prio[0].append('┌─────┐')
        visual_process_queue_sjf_prio[1].append('│     │')
        visual_process_queue_sjf_prio[2].append(process_name)
        visual_process_queue_sjf_prio[3].append('│     │')
        visual_process_queue_sjf_prio[4].append('└─────┘')
        visual_process_queue_sjf_prio[5].append(end_line)

        #DELETE ENDED PROCESS
        del process_queue[0]
        process_queue = sorted(process_queue, key=lambda x: (x[3], x[2]))

        #Draw process queue
        if draw:
          print(f'---- Step {step} - Priority SJF   ----')
          step += 1
          for id_line in range (0,6):
            line = str(visual_process_queue_sjf_prio[id_line])
            for character in "[]'":
              line = line.replace(character, '')
            line = line.replace(', ', '')
            if id_line == 5 and process_queue:
              print(line[:-7])
            else:
              print(line)
          input("Press enter to continue")

        if process_queue:
          waiting_time += time - process_queue[0][1]
      if process_queue:
        process_queue[0][2] -= 1

    #print(process_queue)

    # Change priority in queue
    if time % priority_time == 0:
      for process in process_queue:
        process[3] -= 1
        if process[3] < 0:
          process[3] = 0

    time += 1
    if not process_queue and not process_tab_sjf_prio:
      break

  return waiting_time/numb_processes, visual_process_queue_sjf_prio


# DATA
def load_data(file_name):
  if exists(file_name):
    with open(file_name, 'r') as file:
      arrival_time = [int(x) for x in file.readline().rstrip().split(' ')]
      process_time = [int(x) for x in file.readline().rstrip().split(' ')]
      priority = [int(x) for x in file.readline().rstrip().split(' ')]
      priority_time = int(file.readline().rstrip())
      roundrobin_time = int(file.readline().rstrip())

      processes_tab = []
      for process_id in range(0, len(arrival_time)):
        processes_tab.append([process_id, arrival_time[process_id], process_time[process_id], priority[process_id]])

      return True, processes_tab, priority_time
  else:
    print('File not exitst')
    return False, [], 1

def get_data(processes_tab):
  for process in processes_tab:
    print(f"P{process[0] + 1}: ArrivalTime: {process[1]}, ProcessTime:{process[2]}, Priority:{process[3]}.")
  input('Press enter to conntinue')

def add_data(processes_tab):
  arrival_time = input('Enter ArrivalTime (c for cancel): ')
  if arrival_time == 'c':
    return processes_tab
  process_time= input('Enter ProcessTime (c for cancel): ')
  if process_time == 'c':
    return processes_tab
  priority = input('Enter Priority (c for cancel): ')
  if priority == 'c':
    return processes_tab
  
  try:
    processes_tab.append([processes_tab[-1][0] + 1, int(arrival_time), int(process_time), int(priority)])
    print(f"Process: P{processes_tab[-1][0] + 1}: ArrivalTime: {arrival_time}, ProcessTime: {process_time}, Priority: {priority} added.")
    return processes_tab
  except ValueError:
    print('')
    print('One of value is not number. Process not added')
    input('Press enter to conntinue')

def remove_data(processes_tab):
  process_id = input('Enter process number to delete (c for cancel): ')

  if process_id == 'c':
    return processes_tab
  
  try:
    process_id = int(process_id) - 1
  except ValueError:
    print('')
    print('Value is not number. Process not deleted')
    input('Press enter to conntinue')

  to_del = -1
  for idx in range(0, len(processes_tab)):
    if processes_tab[idx][0] == process_id:
      to_del = idx
  
  if to_del != -1:
    del processes_tab[to_del]
  return processes_tab

def generate_raport(processes_tab, waiting_time_fcfs, visual_process_queue_fcfs, waiting_time_sjf, visual_process_queue_sjf, waiting_time_sjf_prio, visual_process_queue_sjf_prio):
  time = datetime.datetime.now()
  
  raport_path = 'raports/FCFS_SJF_' + time.strftime("%d%m%Y%H%M%S") + '.txt'
  print(raport_path)
  with open(raport_path, 'w+', encoding='UTF-8') as raport:
    raport.write(f'--- {time.strftime("%c")} ---')
    raport.write(f'\nFor data:\n')
    for process in processes_tab:
      raport.write(f"P{process[0] + 1}: ArrivalTime: {process[1]}, ProcessTime:{process[2]}, Priority:{process[3]}.\n")
    raport.write('\n\nFCFS:')
    raport.write(f'\nAvarage waiting time: {waiting_time_fcfs}')
    for line in visual_process_queue_fcfs:
      new_line = str(line)
      new_line = new_line.replace("'",'').replace(',', '').replace('[', '').replace(']', '')
      raport.write(f'\n{new_line}')
    
    raport.write('\n\nSJF:')
    raport.write(f'\nAvarage waiting time: {waiting_time_sjf}')
    for line in visual_process_queue_sjf:
      new_line = str(line)
      new_line = new_line.replace("'",'').replace(',', '').replace('[', '').replace(']', '')
      raport.write(f'\n{new_line}')
    
    raport.write('\n\nSJF WITH PRIORITY:')  
    raport.write(f'\nAvarage waiting time: {waiting_time_sjf_prio}')
    for line in visual_process_queue_sjf_prio:
      new_line = str(line)
      new_line = new_line.replace("'",'').replace(',', '').replace('[', '').replace(']', '')
      raport.write(f'\n{new_line}')

# APP
def main():
  processes_tab = []
  priority_time = 1
  visual_process_queue_fcfs = []
  visual_process_queue_sjf = []
  visual_process_queue_sjf_prio = []

  data_loaded = False
  file_name = ''

  while True:
    print('\n---- Menu ----')
    print('1. Load data')
    if data_loaded:
      print('2. Show data')
      print('3. Add process')
      print('4. Remove process')
      print('5. FCFS')
      print('6. SJF')
      print('7. SJF with Priority')
      print('8. Compare result')
      print('9. Generate raport')
    print('End (q or e)')

    choice = input('Pick position from menu: ')

    if choice == '1':
      file_name = input('Enter data file name: ')
      print('')
      data_loaded, processes_tab, priority_time = load_data(file_name)
    if data_loaded:
      if choice == '2':
        get_data(processes_tab)
      if choice == '3':
        processes_tab = add_data(processes_tab)
      if choice == '4':
        remove_data(processes_tab)
      if choice == '5':
        fcfs(1, processes_tab)
      if choice == '6':
        sjf(1, processes_tab)
      if choice == '7':
        sjf_prio(1, processes_tab, priority_time)
      if choice == '8':
        waiting_time_fcfs = fcfs(0, processes_tab)[0]
        waiting_time_sjf = sjf(0, processes_tab)[0]
        waiting_time_sjf_prio = sjf_prio(0, processes_tab, priority_time)[0]
        print(f'---- Compare results ----')
        print(f"FCFS: {waiting_time_fcfs} \nSJF: {waiting_time_sjf} \nSJF_PRIO: {waiting_time_sjf_prio}")
        input('Press enter to conntinue')
        print('')
      if choice == '9':
        waiting_time_fcfs, visual_process_queue_fcfs = fcfs(0,processes_tab)
        waiting_time_sjf, visual_process_queue_sjf = sjf(0,processes_tab)
        waiting_time_sjf_prio, visual_process_queue_sjf_prio = sjf_prio(0,processes_tab,priority_time)
        
        generate_raport(processes_tab, waiting_time_fcfs, visual_process_queue_fcfs, waiting_time_sjf, visual_process_queue_sjf, waiting_time_sjf_prio, visual_process_queue_sjf_prio)
    if choice == 'q' or choice == 'e' or choice == 'quit' or choice == 'exit':
      break

main()