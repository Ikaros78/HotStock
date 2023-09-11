package com.ssafy.hotstock.domain.news.service;

import com.ssafy.hotstock.domain.news.domain.Media;
import com.ssafy.hotstock.domain.news.domain.MediaRepository;
import java.util.List;
import java.util.Optional;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class MediaServiceImpl implements MediaService {

    private final MediaRepository mediaRepository;

    /**
     * 언론사 번호로 언론사 정보 가져오기
     */
    @Override
    public Media getMediaByMediaCompanyNum(int mediaCompanyNum) {
        Optional<Media> mediaOptional = mediaRepository.findByMediaCompanyNum(mediaCompanyNum);

        Media media;

        if (mediaOptional.isPresent()) {
            media=mediaOptional.get();
        } else {
            media = new Media(mediaCompanyNum);
        }
        return media;
    }

    /**
     * 언론사 정보 저장
     */
    @Override
    public Media saveMedia(Media media) {
        return mediaRepository.save(media);
    }

    /**
     * 모든 언론사 정보 가져오기
     */
    @Override
    public List<Media> getAllMedia() {
        return mediaRepository.findAll();
    }
}