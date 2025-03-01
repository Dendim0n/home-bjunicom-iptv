import m3u8


def filter_m3u(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        m3u = m3u8.loads(f.read())

    titles = set()
    titles_to_remove = set()
    new_segments = []

    for i, segment in enumerate(m3u.segments):
        title = m3u.playlists[i].media[0].title if m3u.playlists else None
        if title:
            titles.append(title)

    for i, segment in enumerate(m3u.segments):
        title = m3u.playlists[i].media[0].title if m3u.playlists else None
        if title:
            if '高清' in title:
                base_title = title.replace('高清', '')
                if base_title in titles:
                    titles_to_remove.add(base_title)


    for i, segment in enumerate(m3u.segments):
        title = m3u.playlists[i].media[0].title if m3u.playlists else None
        if title:
            if title not in titles_to_remove:
                new_segments.append(segment)

    new_m3u = m3u8.M3U8()
    new_m3u.add_header()
    new_segments.sort(key=lambda x: x[0])
    for segment in new_segments:
        new_m3u.add_segment(segment)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_m3u.dumps())


filter_m3u('input.m3u', 'output.m3u')