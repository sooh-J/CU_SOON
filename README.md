# CU_SOON
posco 청년 ai bigdata 아카데미 23기 C4조 빅데이터 프로젝트 CU_SOON
## 프랜차이즈 편의점 매출 증대

1. 대상 : BGF 리테일 (주)CU 편의점
   
2. 데이터 : CU 편의점 판매 데이터 (2021~2022)
   
3. 문제 파악 : 코로나가 안정화되던 2022년에는 CU 편의점의 평균 매출이 경쟁사 대비 양호하게 증가함. \
   그러나 분석을 진행하게 된 당 점포는 점포 운영에 특별한 변화가 없었음에도 **매출액 증가율**이 자사 브랜드 편의점 평균보다 **낮았고**, **객단가**도 전년 대비 **소폭 증가**함. 
   이에 점주 및 본부 분석팀에서 실시하는 문제정의-데이터수집-분석-모델링-적용 절차 프로젝트 중 **분석-모델링** 부분을 진행.
  
4. **분석 내용 : 매출 지표의 부진 원인, 고객 및 상품 유형별 매출 패턴, 기상정보 연계 매출, 구매상품 패턴 분석**


## [발표 자료]

[CU_SOON 최종 발표 PPT](https://github.com/sooh-J/CU_SOON/blob/main/CU_SOON.pdf)


## [프로젝트 구조]
```
.
├── README.md
├── CU_SOON.pdf
├── Preprocessing
│   ├── 2021,2022_sales_rawTO2021,2022_sales_v2
│   ├── User_Pos_items.ipynb
│   ├── df_sales_resultTO2021,2022_sales_raw_v2
│   ├── resultTOdf_sales_result_v2
│   ├── split_question_mark function
│   ├── weather_preprocessing_v2.ipynb
│   └── weather_preprocessing_v3.ipynb
├── Data
│   ├── 데이터.zip
│   ├── README_data.md
│   ├── cvs_items_raw.csv
│   ├── data_for_modeling_v2.csv
│   ├── df_sales_v3.zip
│   ├── users_itemsCategory.csv
│   ├── users_itemsCategory_POS_v2.csv
│   ├── users_itemsCategory_v2.csv
│   └── weather_v3.csv
├── Analysis
│   ├── MODELING.ipynb
│   ├── Customer_Transaction.ipynb
│   ├── Age_Gender_Category.ipynb
│   ├── import_code.ipynb
│   ├── C4_편의점 빅데이터.ipynb
│   ├── items_middle_totalPrice.ipynb
│   ├── nano.save
│   ├── plot_function.py
│   ├── ppt 첨부 표.xlsx
│   ├── project-전처리-한석현-합친 data.ipynb
│   ├── users의 그래프들.ipynb
│   ├── weather_graph.ipynb
│   ├── weather_graph2.ipynb
│   ├── 매출 시계열 김태하.ipynb
│   ├── 매출_시계열_김태하v1.ipynb
│   ├── 월별매출액변동.ipynb
│   └── 월별매출액변동_newgraph.ipynb
└── └── 편의점모델링.ipynb
```


## [CONTRIBUTORS]
POSCO 청년 AI.Bigdata 아카데미 23기 C4조 <br />
<a href="https://github.com/sooh-J/CU_SOON/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=sooh-J/CU_SOON" />
</a>
