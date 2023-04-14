import code_steps.conversion.json_to_csv as conv
import pandas

if __name__ == '__main__':
    keywords = conv.keywords_complete

    count: dict = {}

    for article in keywords:
        for tag in article: 
            count[tag] = 1 if tag not in count else count[tag] + 1 
    
    #sort count based on value
    count = dict(sorted(count.items(), key= lambda y: y[1],reverse=True)) 
    
    print(count)

