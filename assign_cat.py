from cat_dom_map import category_labels
import operator

def assign(domains):
    cat_score = {}
    for cat in category_labels:
        cat_score[cat] = 0
    for dom in domains:
        for cat in category_labels:
            if dom[0] in category_labels[cat]:
                cat_score[cat] += dom[1]
    rank = sorted(cat_score.items(),key=operator.itemgetter(1),reverse=True)
    if rank[0][1] >1:
        return [rank[0][0]]
    elif rank[0][0] == 0:
        return ['others']
    else:
        ans = []
        i = 0
        for r in rank:
            if r[1] == 1 and i<2:
                i +=1
                ans.append(r[0])
            else:
                break
        return ans




