import multiprocessing
from multiprocessing import Pool
import numpy as np
import pandas as pd
from tqdm import tqdm


def parallel_process(process_df, df, n_split=multiprocessing.cpu_count()-1):
    return parallel_process_df(process_df, np.array_split(df,n_split))

def parallel_process_df(func, args,n_processes = multiprocessing.cpu_count()-1):
    '''
    distribute a job to worker by passing given function(job) and splited data as an argument

    '''
    concat_result = pd.DataFrame()
    p = Pool(n_processes)

    with tqdm(total = len(args)) as pbar:
        for _, res in tqdm(enumerate(p.imap_unordered(func, args,))):
            pbar.update()
            concat_result = pd.concat([concat_result,res])
            
    pbar.close()
    p.close()
    p.join()
    return concat_result