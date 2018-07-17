import os, sys
import re


def read_file(filename, batch_size=1024):
    """
    This function generate a dictionary with all drugs, total drug cost and 
    the total number of UNIQUE individuals who have been prescribed a medication
    
    Args:
        filename (str): filepath (relative to the current working directory) 
        
        batch_size: A int (default=1024), this is the number of bytes to be read from the file.
    
    Return:
        A dictionary 
    """

    cols = {}
    with open(filename, "r") as f:
        data = f.readlines(batch_size)
        
        while data:
            for line in data:
                
                # Split the lines by commas and decode line ignoring spanish characters
                line = line.strip('\n')
                line = line.encode('utf-8').decode('ascii', 'ignore')
                regex = re.compile(r"([a-zA-Z0-9*'\`\-\s*\.\/\%\&\(\)\#\_\+(\w+)]+|\d+|\".+?\")", re.UNICODE)
                cells = regex.findall(line)
                
                
                if cells[-1] != 'drug_cost':

                    # create a dict with drug_names, num_prescriber, total_cost, name and last_name if it does not exis
                    if cells[-2] not in cols:
                        cols[cells[-2]]=dict({'num_prescriber':1, 'total_cost':cells[-1], 
                                              'name': cells[1], 'last_name':cells[2]})

                    # Count the number of prescriber for UNIQUE individuals
                    
                    elif cells[-2] in cols:

                        last_price = float(cols[cells[-2]]['total_cost'])
                        count = int(cols[cells[-2]]['num_prescriber'])
                        update = last_price + float(cells[-1])
                        cols[cells[-2]]['total_cost']=update

                        # is the same person if two lines share the same prescriber first and last names
                        if cols[cells[-2]]['name'] != cells[2] and cols[cells[-2]]['last_name'] != cells[1]:
                            cols[cells[-2]]['num_prescriber']=count+1

                        else:
                            cols[cells[-2]]['num_prescriber']=count
                            
                        cols[cells[-2]]['name']= cells[2]
                        cols[cells[-2]]['last_name']= cells[1]

            data = f.readlines(batch_size)
    
        return cols

def save_to_txt(outfilename, filein):
    """
    This function save a file separated by commas that contains the following lines:
    drug_name,num_prescriber,total_cost 
    
    Args:
        filepath (str): path where the file would be saved (relative to the current working directory) 
        
        filein: Is a dictionary of dictionary, with the following structure:
        drug_name = {num_prescriber:, total_cost:, name:, last_name:}
    
    Return:
        None
    """
    with open(outfilename, 'w') as out:
        out.write("drug_name,num_prescriber,total_cost\n")
        for k, v in sorted(filein.items(), key=lambda x: (int(float(x[1]['total_cost']))), reverse=True):
            out.write('{},{},{:d}\n'.format(k, v['num_prescriber'], int(float(v['total_cost']))))
        return None

if __name__ == '__main__':
    # path current directory
    filename = os.path.realpath('.')
    items = os.listdir(os.path.join(filename, 'input'))
    
    # read all the .txt files inside input folder
    for item in items:
        if item.endswith('.txt'):
            filein = os.path.join(filename, 'input', item)
            try:
                mydata = read_file(filein)
                # create a output directory is it does not exist
                output_dir = os.path.join(filename, 'output')
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                save_to_txt(os.path.join(filename, output_dir, 'top_cost_drug.txt'), mydata)
            except Exception as inst:
                print(inst)
