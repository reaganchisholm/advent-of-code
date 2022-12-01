import re

baggage_regulations_raw = open('puzzle_input.txt', 'r').read().split('\n')
baggage_regulations_test = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".split("\n")

def tree_structure(initial_data):
    result = {}
    
    for item in initial_data:
        bag_and_contents_regex = r"^(\w+ \w+) bags contain (.*)"
        bag_and_contents = re.search(bag_and_contents_regex, item)
        bag_type = bag_and_contents[1]
        
        contents_string = bag_and_contents[2][:-1] # [:-1] removes trailing period
        contents_regex = r"([0-9] )*(\w+ \w+) bag"
        contents_tuples = re.findall(contents_regex, contents_string)
        
        bag_contents = []
        for contents_tuple in contents_tuples:
            if contents_tuple[1] != "no other":
                bag_contents.append({
                    "count": int(contents_tuple[0]),
                    "type": contents_tuple[1]
                })
                
        result[bag_type] = bag_contents
        
    return result

bags = tree_structure(baggage_regulations_raw)

def shiny_gold_bag_count(bag_collection, bag_name):
    count = 0
    bag = bag_collection[bag_name]
    
    if len(bag) == 0:
        return count
    else:
        for sub_bag in bag:
            if sub_bag["type"] == "shiny gold":
                count += 1
            count += shiny_gold_bag_count(bag_collection, sub_bag["type"])
        
    return count

def bags_containing_at_least_one_shiny_gold_bag(bag_collection):
    count = 0
    
    for bag_name in bag_collection.keys():
        if shiny_gold_bag_count(bag_collection, bag_name) > 0:
            count += 1

    return count

def bag_count(bag_collection, bag_name):
    count = 0
    top_level_bag = bag_collection[bag_name]
    
    if len(top_level_bag) == 0:
        return count
    else:
        for current_bag in top_level_bag:
            current_bag_type_count = current_bag['count']
            count += current_bag_type_count
            bags_inside_current_bag_type_count = bag_count(bag_collection, current_bag["type"])
            count += bags_inside_current_bag_type_count * current_bag_type_count
        
    return count

shiny_freq_count = bags_containing_at_least_one_shiny_gold_bag(bags)
gold_count = bag_count(bags, 'shiny gold')

print(f"Part 1 -- Bags that can contain a shiny gold: {shiny_freq_count}")
print(f"Part 2 -- How many bags required in a shiny gold bag: {gold_count}")