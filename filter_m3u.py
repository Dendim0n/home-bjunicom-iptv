def filter_and_sort_m3u(input_file, output_file):
    try:
        # 打开输入文件并读取内容
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 按行分割内容
        lines = content.splitlines()

        # 用于存储标题和对应节目的字典
        program_dict = {}
        current_title = None
        current_program = []

        # 遍历每一行
        for line in lines:
            if line.startswith('#EXTINF:'):
                # 提取标题
                title_start = line.find(',') + 1
                current_title = line[title_start:]
                if '高清' in current_title:
                    base_title = current_title.replace('高清', '')
                    # 如果标题包含“高清”，将基础标题标记为要移除
                    program_dict[base_title] = None
                    current_title = None
                    current_program = []
                else:
                    current_program = [line]
            elif line and current_title:
                # 收集节目段的行
                current_program.append(line)
                program_dict[current_title] = '\n'.join(current_program)
                current_title = None
                current_program = []

        # 遍历每一行
        for line in lines:
            if line.startswith('#EXTINF:'):
                # 提取标题
                title_start = line.find(',') + 1
                current_title = line[title_start:]
                if '高清' in current_title:
                    base_title = current_title.replace('高清', '')
                    # 如果标题包含“高清”，将基础标题标记为要移除
                    program_dict[base_title] = None

        # 移除标记为要移除的标题及其对应的节目
        program_dict = {k: v for k, v in program_dict.items() if v is not None}

        # 按标题排序
        sorted_programs = sorted(program_dict.items(), key=lambda item: item[0])

        # 生成新的 M3U 内容
        new_m3u_content = '#EXTM3U\n'
        for _, program in sorted_programs:
            new_m3u_content += program + '\n'

        # 将新的 M3U 内容写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(new_m3u_content)

        print(f"过滤并排序完成，结果已保存到 {output_file}")
    except FileNotFoundError:
        print(f"文件 {input_file} 未找到，请检查文件路径。")
    except Exception as e:
        print(f"发生错误: {e}")


# 调用函数进行过滤和排序操作
filter_and_sort_m3u('input.m3u', 'output.m3u')