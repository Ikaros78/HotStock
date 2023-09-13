package com.ssafy.hotstock.domain.stocktheme.service;

import com.ssafy.hotstock.domain.stocktheme.domain.StockTheme;
import com.ssafy.hotstock.domain.stock.domain.Stock;
import com.ssafy.hotstock.domain.theme.domain.Theme;

import java.util.List;
import java.util.Optional;

public interface StockThemeService {
    StockTheme save(StockTheme stockTheme);
    Optional<StockTheme> findById(Long id);
    List<StockTheme> findAll();
    void delete(StockTheme stockTheme);
}