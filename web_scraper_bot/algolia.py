from algoliasearch import algoliasearch as Algo
#ALGOLIA SEARCH

#Authentication
client = Algo.Client('X8O4N0BKMN','5e75ab8ec734dc6efeafa378d87d5cc9')  #app ID and Admin APIKey
index = client.init_index('')
