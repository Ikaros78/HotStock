package com.ssafy.hotstock.domain.keywordtheme.repository;

import com.ssafy.hotstock.domain.keywordtheme.domain.KeywordTheme;
import com.ssafy.hotstock.domain.theme.domain.Theme;
import io.swagger.v3.oas.annotations.Hidden;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;
import org.springframework.data.rest.core.annotation.RestResource;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

//@Repository
@Repository
@Hidden
public interface KeywordThemeRepository extends JpaRepository<KeywordTheme, Long> {

    List<KeywordTheme> findAllById(Long id);

    @Query("SELECT kt FROM KeywordTheme kt JOIN FETCH kt.keyword WHERE kt.theme.id = :themeId")
    List<KeywordTheme> findByThemeId(Long themeId);


    @Query("SELECT kt FROM KeywordTheme kt JOIN FETCH kt.theme WHERE kt.keyword.id = :keywordId")
    List<KeywordTheme> findByKeywordIdWithTheme(@Param("keywordId") Long keywordId);
}
