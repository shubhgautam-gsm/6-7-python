# prince_comment="nonsense u are always wrong"

# prince_comment=prince_comment.replace('nonsens','***')

# print(prince_comment)  # Output: 2061


prince_comment=input('prince write comment:')
# if(bad_words_dictonary in prince_comment ):
#     prince_comment= prince_comment.replace(prince_comment,'***')

if('nonsense' in prince_comment or 'fool' in prince_comment or 'nakamno' in prince_comment):
    prince_comment=prince_comment.replace('nonsense', '***')
    prince_comment=prince_comment.replace('fool', '***')
    prince_comment=prince_comment.replace('nakamno', '***')
    prince_comment=prince_comment.replace('nonsense', '***')
    
    print(prince_comment)