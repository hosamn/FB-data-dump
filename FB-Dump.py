from facebook_scraper import get_posts
from json import dumps


# i = 1

# for post in get_posts('mwrifb', pages=10):
#     print('post ', i, post['text'][:50])

#     with open('C:/Users/H/Desktop/myFBDump.txt', 'ab') as myfile:

#         dic2str = dumps(post, indent=4, sort_keys=True, default=str)

#         dic2str = dic2str.encode('utf8')

#         myfile.write(dic2str)

#     i += 1


with open('C:/Users/H/Desktop/myFBDump.txt', 'ab') as myfile:

    i = 1

    for post in get_posts('mwrifb', pages=10):

        print('post ', i, post['text'][:50])

        dic2str = dumps(post, indent=4, sort_keys=True, default=str)
        dic2str = dic2str.encode('utf8')
        myfile.write(dic2str)

        i += 1
