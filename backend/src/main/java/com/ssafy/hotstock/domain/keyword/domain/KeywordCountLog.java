package com.ssafy.hotstock.domain.keyword.domain;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Getter
@Setter
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class KeywordCountLog {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name ="count_log_id")
    private Long id;

    @Column(name = "keywordContent")
    private String keywordContent;

    @Column(name = "sub_count")
    private int subCount;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name ="check_point_id")
    private KeywordCheckPoint keywordCheckPoint;
}
