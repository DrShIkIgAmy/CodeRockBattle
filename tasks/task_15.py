

def get_variations_single(hint: list, order= 5):
    hint = hint[0]
    if hint > order:
        return None
    if hint == order:
        return [[1]*order]
    lst = []
    for i in range(order - hint + 1):
        tmp = [0]*i+[1]*hint+[0]*(order - hint -i)
        lst.append(tmp)
    return lst

def get_variations_multi(hint: list, order= 5):
    h_len = len(hint)
    if h_len == 1:
        return get_variations_single(hint, order)
    res_variation = []
    for i in range(order):
        rec_res = get_variations_multi(hint[1:], order-i- 1 - hint[0])
        if rec_res == None:
            break
        for rc_rs in rec_res:
            tmp = [0]*i+[1]*hint[0]+[0]+rc_rs
            res_variation.append(tmp)
    return res_variation

def build_vocs(cols_hits, rows_hits, order = 5):
    col_voc = {}
    row_voc = {}
    for i in range(order):
        col_voc[i] = get_variations_multi(cols_hits[i], order)
        row_voc[i] = get_variations_multi(rows_hits[i], order)
    return col_voc, row_voc




def match_rows(col_voc: set, row_voc: set, order= 5):
    voc = {}
    for col in col_voc:
        mtch = []
        for guesses_col in col_voc[col]:
            row_gs = {}
            for inc in range(order):
                vect = []
                for guesses_row in row_voc[inc]:
                    if guesses_col[inc] == guesses_row[col]:
                        vect.append(guesses_row)
                row_gs[inc] = vect
            mtch.append((guesses_col, row_gs))
        voc[col] = mtch
    return voc

def remove_fake_guess(row, voc, order=5):
    for i in range(order):
        for ii in range(len(voc[i])):
            col_g = voc[i][ii]
            rm_lines = []
            for gg in range(len(col_g[1][row])):
                row_g = col_g[1][row][gg]
                flg = True
                for j in [x for x in range(order) if x!=i]:
                    isContains = False
                    for col_gg in voc[j]:
                        if col_gg[1][row].count(row_g) > 0:
                            isContains = True
                    flg = isContains
                    if flg == False:
                        break
                if flg == False:
                    rm_lines.append(row_g)
            for ii in rm_lines:
                col_g[1][row].remove(ii)
    return voc

def is_contains_empty_guesses(guess):
    for i in guess[1]:
        if len(guess[1][i]) == 0:
            return True
    return False

def retrieve_solution(voc, order=5):
    res_voc = {}
    for i in range(order):
        tmp_sol = []
        for guess in voc[i]:
            if not is_contains_empty_guesses(guess):
                tmp_sol.append(guess[0])
        res_voc[i] = tmp_sol
    return res_voc


def col_to_row(cols, order=5):
    rows = []
    for i in range(order):
        row = []
        for j in range(order):
            row.append(cols[j][i])
        rows.append(row)
    return rows

def combine_sol(sol_voc, voc, cur_col, rows, order=5):
    if cur_col<0:
        return 
    for i in voc[cur_col]:
        sol_voc[cur_col] = i
        combine_sol(sol_voc, voc, cur_col-1,rows)
        cols = [sol_voc[i] for i in sol_voc]
        rows_ = col_to_row(cols)
        flg = True
        for j in range(order):
            if rows[j].count(rows_[j]) == 0:
                flg = False
                break
        if flg == True:
            break


def solve(cols_hin, rows_hint, order= 5):
    cols, rows = build_vocs(cols_hin, rows_hint, order)
    voc = match_rows(cols, rows)
    for row_inc in range(order):
        voc = remove_fake_guess(row_inc, voc)
    for row_inc in range(order):
        voc = remove_fake_guess(row_inc, voc)
    rv = retrieve_solution(voc)
    res_voc = {}
    combine_sol(res_voc, rv, 4, rows)
    cols = []
    for i in res_voc:
        cols.append(res_voc[i])
    rows = col_to_row(cols)
    for i in rows:
        i.reverse()
        out_str = ''
        for char in i:
            out_str += 'X' if char==1 else '-'
        print(out_str)




    
solve([[2],[2],[4],[1,1,1],[1,1]],[[3],[3],[4],[1],[2]])