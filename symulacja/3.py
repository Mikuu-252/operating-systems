from os.path import exists
import datetime

#algorithm
def fifo(draw, references_tab, frames_size):
  edit_number = 0
  step = 1
  frames = []
  for i in range(0,frames_size):
    frames.append('-')
  visual_fifo = []


  # Prepare visual list
  for key in frames:
    visual_fifo.append([])
    visual_fifo.append([])
    visual_fifo.append([])

  # FIFO
  for reference in references_tab:
    last_edit = -1
    if not reference in frames:
      frames[edit_number % frames_size] = reference
      edit_number += 1
      last_edit = reference

    # Create visual list
    for idx in range(0, len(frames)):
      if frames[idx] == last_edit:
        visual_fifo[0 + idx*3].append('┌───┐')
        if frames[idx] < 10:
          visual_fifo[1 + idx*3].append(f'│ {frames[idx]} │')
        else:
          visual_fifo[1 + idx*3].append(f'│{frames[idx]} │')
        visual_fifo[2 + idx*3].append('└───┘')
      else:
        visual_fifo[0 + idx*3].append('     ')
        if frames[idx] == '-' or frames[idx] < 10:
          visual_fifo[1 + idx*3].append(f'  {frames[idx]}  ')
        else:
          visual_fifo[1 + idx*3].append(f' {frames[idx]}  ')
        visual_fifo[2 + idx*3].append('     ')
    # draw
    if draw:
      print(f'---- FIFO Step: {step} ----')
      for line in visual_fifo:
        new_line = str(line)
        for char in "[],'":
          new_line = new_line.replace(char,'')
        print(new_line)
      input('Press enter to continue')
    step += 1
  if draw:
    print(f'Missing pages: {edit_number}')
  return edit_number, visual_fifo

def opt(draw, references_tab, frames_size):
  frames = []
  for i in range(0,frames_size):
    frames.append('-')
  edit_number = 0
  step = 1
  visual_opt = []

  # Prepare visual list
  for key in frames:
    visual_opt.append([])
    visual_opt.append([])
    visual_opt.append([])

  # OPT
  for reference in references_tab:
    last_edit = -1

    if not reference in frames:
      references_to_check = references_tab[step:]
      what_frame = 0
      highest_index = 0

      for frame in frames:
        if frame == '-':
          what_frame = '-'
          break
        if step > 3:
          if not frame in references_to_check:
            what_frame = frame
            break

        if frame in references_to_check:
          if references_tab.index(frame, step-1) > highest_index:
            highest_index = references_tab.index(frame, step-1)
            what_frame = frame
      
      frames[frames.index(what_frame)] = reference
      edit_number += 1
      last_edit = reference

    # Create visual list
    for idx in range(0, len(frames)):
      if frames[idx] == last_edit:
        visual_opt[0 + idx*3].append('┌───┐')
        if frames[idx] < 10:
          visual_opt[1 + idx*3].append(f'│ {frames[idx]} │')
        else:
          visual_opt[1 + idx*3].append(f'│{frames[idx]} │')
        visual_opt[2 + idx*3].append('└───┘')
      else:
        visual_opt[0 + idx*3].append('     ')
        if frames[idx] == '-' or frames[idx] < 10:
          visual_opt[1 + idx*3].append(f'  {frames[idx]}  ')
        else:
          visual_opt[1 + idx*3].append(f' {frames[idx]}  ')
        visual_opt[2 + idx*3].append('     ')
    # draw
    if draw:
      print(f'---- OPT Step: {step} ----')
      for line in visual_opt:
        new_line = str(line)
        for char in "[],'":
          new_line = new_line.replace(char,'')
        print(new_line)
      input('Press enter to continue')
    step += 1
  if draw:
    print(f'Missing pages: {edit_number}')
  return edit_number, visual_opt

def lru(draw, references_tab, frames_size):
  frames = []
  for i in range(0,frames_size):
    frames.append('-')
  edit_number = 0
  step = 1
  visual_lru = []
  last_changes = []

  # Prepare visual list
  for key in frames:
    visual_lru.append([])
    visual_lru.append([])
    visual_lru.append([])
    last_changes.append(-1)

  # LRU
  for reference in references_tab:
    last_edit = -1
    if not reference in frames:
      if '-' in frames:
          what_frame = frames.index('-')
      else:
          what_frame = last_changes.index(min(last_changes))

      last_changes[what_frame] = step-1
      frames[what_frame] = reference

      edit_number += 1
      last_edit = reference
    else:
      what_frame = frames.index(reference)
      last_changes[what_frame] = step-1

    # Create visual list
    for idx in range(0, len(frames)):
      if frames[idx] == last_edit:
        visual_lru[0 + idx*3].append('┌───┐')
        if frames[idx] < 10:
          visual_lru[1 + idx*3].append(f'│ {frames[idx]} │')
        else:
          visual_lru[1 + idx*3].append(f'│{frames[idx]} │')
        visual_lru[2 + idx*3].append('└───┘')
      else:
        visual_lru[0 + idx*3].append('     ')
        if frames[idx] == '-' or frames[idx] < 10:
          visual_lru[1 + idx*3].append(f'  {frames[idx]}  ')
        else:
          visual_lru[1 + idx*3].append(f' {frames[idx]}  ')
        visual_lru[2 + idx*3].append('     ')
    # draw
    if draw:
      print(f'---- LRU Step: {step} ----')
      for line in visual_lru:
        new_line = str(line)
        for char in "[],'":
          new_line = new_line.replace(char,'')
        print(new_line)
      input('Press enter to continue')
    step += 1
  if draw:
    print(f'Missing pages: {edit_number}')
  return edit_number, visual_lru

def lfu(draw, references_tab, frames_size):
  frames = []
  for i in range(0,frames_size):
    frames.append('-')
  edit_number = 0
  step = 1
  visual_lfu = []
  number_of_changes = []
  
  for idx in range(0, max(references_tab)+1):
    number_of_changes.append(0)

  # Prepare visual list
  for key in frames:
    visual_lfu.append([])
    visual_lfu.append([])
    visual_lfu.append([])

  # LFU
  for reference in references_tab:
    last_edit = -1
    if not reference in frames:
      if '-' in frames:
          what_frame = frames.index('-')
      else:
          used_value  = []
          for frame in frames:
            used_value.append(number_of_changes[frame])
          what_frame = used_value.index(min(used_value))

      number_of_changes[reference] += 1
      frames[what_frame] = reference

      edit_number += 1
      last_edit = reference
    else:
      used_value  = []
      for frame in frames:
        used_value.append(number_of_changes[frame])
      what_frame = used_value.index(min(used_value))
      number_of_changes[reference] += 1

    # Create visual list
    for idx in range(0, len(frames)):
      if frames[idx] == last_edit:
        visual_lfu[0 + idx*3].append('┌───┐')
        if frames[idx] < 10:
          visual_lfu[1 + idx*3].append(f'│ {frames[idx]} │')
        else:
          visual_lfu[1 + idx*3].append(f'│{frames[idx]} │')
        visual_lfu[2 + idx*3].append('└───┘')
      else:
        visual_lfu[0 + idx*3].append('     ')
        if frames[idx] == '-' or frames[idx] < 10:
          visual_lfu[1 + idx*3].append(f'  {frames[idx]}  ')
        else:
          visual_lfu[1 + idx*3].append(f' {frames[idx]}  ')
        visual_lfu[2 + idx*3].append('     ')
    # draw
    if draw:
      print(f'---- LFU Step: {step} ----')
      for line in visual_lfu:
        new_line = str(line)
        for char in "[],'":
          new_line = new_line.replace(char,'')
        print(new_line)
      input('Press enter to continue')
    step += 1
  if draw:
    print(f'Missing pages: {edit_number}')
  return edit_number, visual_lfu


#data
def load_data(file_name, references_tab, frames_size):
  if exists(file_name):
    with open(file_name, 'r') as file:
      references_tab = []
      references_tab = [int(x) for x in file.readline().rstrip().split(' ')]
    
      frames_size = int(file.readline().rstrip())
      return True, references_tab, frames_size
  else:
    print('File not exitst')
    return False, [], 0

def get_data(references_tab):
  print(f'References: {references_tab}')
  input('Press enter to conntinue')

def add_data(references_tab):
  new_reference = input('What reference what you add(c for cancel): ')
  if new_reference == 'c':
    return references_tab
  new_reference = int(new_reference)
  if new_reference < 0:
    print('Your number must be greter then 0')
    return references_tab
  references_tab.append(new_reference)
  return references_tab

def remove_data(references_tab):
  index_reference = input('What reference what you remove(c for cancel): ')
  if index_reference == 'c':
    return references_tab
  index_reference = int(index_reference)
  if index_reference < 0 or index_reference >= len(references_tab):
    print(f'Your number must be greter then 0 or lower then {len(references_tab)}')
    return references_tab
  references_tab.pop(index_reference)
  return references_tab

# raport
def compare_results(references_tab, frames_size):
  missing_pages_fifo = fifo(0, references_tab, frames_size)[0]
  missing_pages_opt = opt(0, references_tab, frames_size)[0]
  missing_pages_lru = lru(0, references_tab, frames_size)[0]
  missing_pages_lfu = lfu(0, references_tab, frames_size)[0]
  print(f'---- Compare results ----')
  print(f'FIFO :{missing_pages_fifo}')
  print(f'OPT :{missing_pages_opt}')
  print(f'LRU :{missing_pages_lru}')
  print(f'LFU :{missing_pages_lfu}')
  input('Press enter to continue')

def generate_raport(references_tab, frames_size):
  missing_pages_fifo, visual_fifo = fifo(0, references_tab, frames_size)
  missing_pages_opt,  visual_opt = opt(0, references_tab, frames_size)
  missing_pages_lru,  visual_lru = lru(0, references_tab, frames_size)
  missing_pages_lfu,  visual_lfu = lfu(0, references_tab, frames_size)
  time = datetime.datetime.now()
  
  raport_path = 'raports/FIFO_OPT_LRU_LFU_' + time.strftime("%d%m%Y%H%M%S") + '.txt'
  print(raport_path)
  with open(raport_path, 'w+', encoding='UTF-8') as raport:
    raport.write(f'--- {time.strftime("%c")} ---\n')
    raport.write(f"References: {references_tab}\n")

    raport.write('\nFIFO:')
    raport.write(f'\nMissing pages: {missing_pages_fifo}')
    for line in visual_fifo:
      new_line = str(line)
      new_line = new_line.replace("'",'').replace(',', '').replace('[', '').replace(']', '')
      raport.write(f'\n{new_line}')

    raport.write('\nOPT:')
    raport.write(f'\nMissing pages: {missing_pages_opt}')
    for line in visual_opt:
      new_line = str(line)
      new_line = new_line.replace("'",'').replace(',', '').replace('[', '').replace(']', '')
      raport.write(f'\n{new_line}')

    raport.write('\nLRU:')
    raport.write(f'\nMissing pages: {missing_pages_lru}')
    for line in visual_lru:
      new_line = str(line)
      new_line = new_line.replace("'",'').replace(',', '').replace('[', '').replace(']', '')
      raport.write(f'\n{new_line}')

    raport.write('\nLFU:')
    raport.write(f'\nMissing pages: {missing_pages_lfu}')
    for line in visual_lfu:
      new_line = str(line)
      new_line = new_line.replace("'",'').replace(',', '').replace('[', '').replace(']', '')
      raport.write(f'\n{new_line}')

#APP
def main():
  data_loaded = False
  file_name = ''

  references_tab = []
  frames_size = 0
  frames = []

  visual_fifo = []
  visual_opt = []
  visual_lru = []
  visual_lfu = []

  while True:
    print('\n---- Menu ----')
    print('1. Load data')
    if data_loaded:
      print('2. Show data')
      print('3. Add reference')
      print('4. Remove reference')
      print('5. FIFO')
      print('6. OPT')
      print('7. LRU')
      print('8. LFU')
      print('9. Compare result')
      print('10. Generate raport')
    print('End (q or e)')

    choice = input('Pick position from menu: ')

    if choice == '1':
      file_name = input('Enter data file name: ')
      print('')
      data_loaded, references_tab, frames_size = load_data(file_name, references_tab, frames_size)
    if data_loaded:
      if choice == '2':
        get_data(references_tab)
      if choice == '3':
        references_tab = add_data(references_tab)
      if choice == '4':
        references_tab = remove_data(references_tab)
      if choice == '5':
        fifo(1, references_tab, frames_size)
      if choice == '6':
        opt(1, references_tab, frames_size)
      if choice == '7':
        lru(1, references_tab, frames_size)
      if choice == '8':
        lfu(1, references_tab, frames_size)
      if choice == '9':
        compare_results(references_tab, frames_size)
      if choice == '10':
        generate_raport(references_tab, frames_size)

    if choice == 'q' or choice == 'e' or choice == 'quit' or choice == 'exit':
      break

main()