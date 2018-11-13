import json
import hw_quiz


def save(filename, data):
    to_save = hw_quiz.readcurrency(data)
    new_dict = {"data":to_save}
    with open(filename, "w") as output_file:
	    json.dump(new_dict, output_file)
    

save("output.json", "currency.txt")