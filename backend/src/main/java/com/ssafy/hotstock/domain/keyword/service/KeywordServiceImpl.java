package com.ssafy.hotstock.domain.keyword.service;


import com.ssafy.hotstock.domain.keyword.domain.Keyword;
import com.ssafy.hotstock.domain.keyword.domain.KeywordRepository;
import com.ssafy.hotstock.domain.keyword.service.KeywordService;
import com.ssafy.hotstock.domain.keywordsummary.service.KeywordSummaryService;

import com.ssafy.hotstock.domain.keywordsummary.domain.KeywordSummary;

import com.ssafy.hotstock.domain.news.domain.News;
import com.ssafy.hotstock.domain.news.service.NewsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class KeywordServiceImpl implements KeywordService {

    @Autowired
    private KeywordRepository keywordRepository;

    @Autowired
    private NewsService newsService;

    @Autowired
    private KeywordSummaryService keywordSummaryService;

    @Override
    public Keyword insertKeyword(Keyword keyword) {
        News news = newsService.insertNews(keyword.getNews());
        KeywordSummary keywordSummary = keywordSummaryService.insertKeywordSummary(keyword.getKeywordSummary());
        keyword.setNews(news);
        keyword.setKeywordSummary(keywordSummary);

        return keywordRepository.save(keyword);
    }

    @Override
    public Optional<Keyword> getKeywordById(Long id) {
        return keywordRepository.findById(id);
    }

    @Override
    public List<Keyword> getAllKeywords() {
        return keywordRepository.findAll();
    }

    @Override
    public Keyword updateKeyword(Keyword keyword) {

        News updatedNews = newsService.updateNews(keyword.getNews());
        KeywordSummary updatedKeywordSummary = keywordSummaryService.updateKeywordSummary(keyword.getKeywordSummary());
        keyword.setNews(updatedNews);
        keyword.setKeywordSummary(updatedKeywordSummary);

        return keywordRepository.save(keyword);
    }

    @Override
    public void deleteKeyword(Long id) {
        Keyword existingKeyword = keywordRepository.findById(id).orElse(null);
        if (existingKeyword != null) {
            newsService.deleteNews(existingKeyword.getNews().getId());
            keywordSummaryService.deleteKeywordSummary(existingKeyword.getKeywordSummary().getId());
        }

        keywordRepository.deleteById(id);
    }

}
