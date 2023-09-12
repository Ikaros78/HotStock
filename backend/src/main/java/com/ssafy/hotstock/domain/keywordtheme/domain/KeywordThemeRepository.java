package com.ssafy.hotstock.domain.keywordtheme.domain;

import com.ssafy.hotstock.domain.keywordtheme.domain.KeywordTheme;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface KeywordThemeRepository extends JpaRepository<KeywordTheme, Long> {
    List<KeywordTheme> findAllById(Long id);
}
