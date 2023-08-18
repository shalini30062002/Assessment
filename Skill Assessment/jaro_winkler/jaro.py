from jarowinkler import jaro_similarity

investor_list = ['Dr Guruprasad', 'Thangamani Prabhakaran', 'Kanchan Ochani', 'Deepak Chirunomula', 'N K Choudhary', 'Varun Dave', 'K G Vasani', 'Sephoy Ramkumar']
eps_investor_list = ['Guruprasad', 'T Prabhakaran', 'Sanchita Ochani', 'Chirunomula', 'Niket Kumar Choudhary', 'Varun Dave', 'Ketankumargordhanbhaiv', 'Ramkumar' ]

def match_investors():
  matches = []
  for investor in investor_list:
    for eps_investor in eps_investor_list:
      similarity = jaro_similarity(investor, eps_investor)
      matches.append((investor, eps_investor, similarity))

  return matches

matches = match_investors()

for match in matches:
  print(match)
