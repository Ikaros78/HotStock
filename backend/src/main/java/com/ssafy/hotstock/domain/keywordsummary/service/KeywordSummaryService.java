package com.ssafy.hotstock.domain.keywordsummary.service;

import com.ssafy.hotstock.domain.keywordsummary.domain.KeywordSummary;

import java.util.List;
import java.util.Optional;

public interface KeywordSummaryService {

    KeywordSummary insertKeywordSummary(KeywordSummary keywordSummary);

    Optional<KeywordSummary> getKeywordSummaryById(Long id);

    List<KeywordSummary> getAllKeywordSummary();

    KeywordSummary updateKeywordSummary(KeywordSummary keywordSummary);

    void deleteKeywordSummary(Long id);

}
