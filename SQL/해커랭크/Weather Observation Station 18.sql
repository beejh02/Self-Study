SELECT ABS(ROUND(MAX(LAT_N),4)-ROUND(MIN(LAT_N),4) ) +ABS(ROUND(MAX(LONG_W),4) -ROUND(MIN(LONG_W),4)) FROM STATION;
