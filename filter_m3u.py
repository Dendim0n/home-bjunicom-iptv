try:
    m3u_list = []
    needs_removed = []
    result_str = "#EXTM3U\n"
    with open('input.m3u', 'r', encoding='utf-8') as file:
        name = ''
        link = ''
        for line in file:
            # 去除行尾的换行符
            line = line.rstrip()
            if 'EXTM3U' in line:
                continue
            if '#EXTINF' in line:
                name = line.replace('#EXTINF:-1','')
                name = name.replace('#EXTINF:','')
                if '高清' in name:
                    needs_removed.append(name.replace('高清',''))
            if 'http' in line:
                link = line
                m3u_list.append([name, link])
        result = []
        for m in m3u_list:
            if m[0] not in needs_removed:
                result.append(m)
        result = sorted(result, key=lambda x: x[0])
        for m in result:
            item = "#EXTINF:-1," + "\n".join(m) + '\n'
            result_str += item
            
    with open('output.m3u', 'w', encoding='utf-8') as file:
    # 将字符串写入文件
        file.write(result_str)
        
except FileNotFoundError:
    print("文件未找到，请检查文件路径。")