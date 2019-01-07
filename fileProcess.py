import praw
# import pandas as pd
import logging
import csv

reddit = praw.Reddit(client_id=' ', \
    client_secret=' ', \
    user_agent=' ', \
    username=' ', \
    password=' ')

subreddit = reddit.subreddit('datascience') #put subreddit here
top_subreddit = subreddit.hot(limit=1) #put limit of threads to fetch
author_name = 'coffeecoffeecoffeee' # TODO: implement author based comment fetch

comments_dict = {}

for submission in top_subreddit:
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    for comment in all_comments:
        # print((comment.body).encode('utf-8'), comment.author.id)
        try:
            author = (comment.author.name).encode('utf-8')
            encoded_comment = (comment.body).encode('utf-8')
            if author in comments_dict:
                comments_dict[author].append(encoded_comment)
            else:
                comments_dict[author] = []
                comments_dict[author].append(encoded_comment)
        except AttributeError as error:
            # Output expected AttributeErrors.
            logging.warning('attr error')
        except Exception as exception:
            # Output unexpected Exceptions.
            logging.warning('exception')

# print(comments_dict)

with open(author_name + ".csv", "wb") as outfile:
    writer = csv.writer(outfile)
    #writer.writerow(comments_dict.keys())
    writer.writerows(zip(*comments_dict.values()))

