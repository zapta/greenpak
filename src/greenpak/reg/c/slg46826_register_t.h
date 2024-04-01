/* ===========================================================================
 * This header is based on original project of:
 * https://github.com/tanakamasayuki/I2C_SLG
 *
 *  ..which was then forked & worked on up by us/MoTeC (Pty) Ltd :
 *  https://github.com/motec-research/I2C_SLG
 *
 * In this instance we interesed in the header only.
 * ===========================================================================
 *
 *  You should Not include this file directly in your C code, use the provided
 *  slg46826_reg.h
 *
 *  Use: the type below as defined can be included into C/C++ files but it
 *  may also used by a Python parser that doesn't want to see here anything
 *  but the C.
 *
 *  Note: if you modify how slg_register_t below is written, you may break
 *  its parsing by the Python command line utility provided.
 */

typedef struct {
  union {
    struct {
      union {
        uint8_t reg_00;
      };
      union {
        uint8_t reg_01;
      };
      union {
        uint8_t reg_02;
      };
      union {
        uint8_t reg_03;
      };
      union {
        uint8_t reg_04;
      };
      union {
        uint8_t reg_05;
      };
      union {
        uint8_t reg_06;
      };
      union {
        uint8_t reg_07;
      };
      union {
        uint8_t reg_08;
      };
      union {
        uint8_t reg_09;
      };
      union {
        uint8_t reg_0a;
      };
      union {
        uint8_t reg_0b;
      };
      union {
        uint8_t reg_0c;
      };
      union {
        uint8_t reg_0d;
      };
      union {
        uint8_t reg_0e;
      };
      union {
        uint8_t reg_0f;
      };
      union {
        uint8_t reg_10;
      };
      union {
        uint8_t reg_11;
      };
      union {
        uint8_t reg_12;
      };
      union {
        uint8_t reg_13;
      };
      union {
        uint8_t reg_14;
      };
      union {
        uint8_t reg_15;
      };
      union {
        uint8_t reg_16;
      };
      union {
        uint8_t reg_17;
      };
      union {
        uint8_t reg_18;
      };
      union {
        uint8_t reg_19;
      };
      union {
        uint8_t reg_1a;
      };
      union {
        uint8_t reg_1b;
      };
      union {
        uint8_t reg_1c;
      };
      union {
        uint8_t reg_1d;
      };
      union {
        uint8_t reg_1e;
      };
      union {
        uint8_t reg_1f;
      };
      union {
        uint8_t reg_20;
      };
      union {
        uint8_t reg_21;
      };
      union {
        uint8_t reg_22;
      };
      union {
        uint8_t reg_23;
      };
      union {
        uint8_t reg_24;
      };
      union {
        uint8_t reg_25;
      };
      union {
        uint8_t reg_26;
      };
      union {
        uint8_t reg_27;
      };
      union {
        uint8_t reg_28;
      };
      union {
        uint8_t reg_29;
      };
      union {
        uint8_t reg_2a;
      };
      union {
        uint8_t reg_2b;
      };
      union {
        uint8_t reg_2c;
      };
      union {
        uint8_t reg_2d;
      };
      union {
        uint8_t reg_2e;
      };
      union {
        uint8_t reg_2f;
      };
      union {
        uint8_t reg_30;
      };
      union {
        uint8_t reg_31;
      };
      union {
        uint8_t reg_32;
      };
      union {
        uint8_t reg_33;
      };
      union {
        uint8_t reg_34;
      };
      union {
        uint8_t reg_35;
      };
      union {
        uint8_t reg_36;
      };
      union {
        uint8_t reg_37;
      };
      union {
        uint8_t reg_38;
      };
      union {
        uint8_t reg_39;
      };
      union {
        uint8_t reg_3a;
      };
      union {
        uint8_t reg_3b;
      };
      union {
        uint8_t reg_3c;
      };
      union {
        uint8_t reg_3d;
      };
      union {
        uint8_t reg_3e;
      };
      union {
        uint8_t reg_3f;
      };
      union {
        uint8_t reg_40;
      };
      union {
        uint8_t reg_41;
      };
      union {
        uint8_t reg_42;
      };
      union {
        uint8_t reg_43;
      };
      union {
        uint8_t reg_44;
      };
      union {
        uint8_t reg_45;
      };
      union {
        uint8_t reg_46;
      };
      union {
        uint8_t reg_47;
      };
      union {
        uint8_t reg_48;
      };
      union {
        uint8_t reg_49;
      };
      union {
        uint8_t reg_4a;
      };
      union {
        uint8_t reg_4b;
      };
      union {
        uint8_t reg_4c;
      };
      union {
        uint8_t reg_4d;
      };
      union {
        uint8_t reg_4e;
      };
      union {
        uint8_t reg_4f;
      };
      union {
        uint8_t reg_50;
      };
      union {
        uint8_t reg_51;
      };
      union {
        uint8_t reg_52;
      };
      union {
        uint8_t reg_53;
      };
      union {
        uint8_t reg_54;
      };
      union {
        uint8_t reg_55;
      };
      union {
        uint8_t reg_56;
      };
      union {
        uint8_t reg_57;
      };
      union {
        uint8_t reg_58;
      };
      union {
        uint8_t reg_59;
      };
      union {
        uint8_t reg_5a;
      };
      union {
        uint8_t reg_5b;
      };
      union {
        uint8_t reg_5c;
      };
      union {
        uint8_t reg_5d;
      };
      union {
        uint8_t reg_5e;
      };
      union {
        uint8_t reg_5f;
      };
      union {
        struct {
          uint8_t io_fast_pull_up_down_enable: 1; // [60H(0), 768:768]
          uint8_t i2c_mode_selection: 1;          // [60H(1), 769:769]
          uint8_t pad_32__ : 6;
        };
        uint8_t reg_60;
      };
      union {
        struct {
          uint8_t io0_input_mode_configuration: 2;          // [61H(0), 777:776]
          uint8_t io0_output_mode_configuration: 2;         // [61H(2), 779:778]
          uint8_t io0_pull_up_down_resistance_selection: 2; // [61H(4), 781:780]
          uint8_t io0_pull_up_down_selection: 1;            // [61H(6), 782:782]
          uint8_t io0_output_enable: 1;                     // [61H(7), 783:783]
        };
        uint8_t reg_61;
      };
      union {
        struct {
          uint8_t io1_input_mode_configuration: 2;          // [62H(0), 785:784]
          uint8_t io1_output_mode_configuration: 2;         // [62H(2), 787:786]
          uint8_t io1_pull_up_down_resistance_selection: 2; // [62H(4), 789:788]
          uint8_t io1_pull_up_down_selection: 1;            // [62H(6), 790:790]
          uint8_t pad_01__: 1;
        };
        uint8_t reg_62;
      };
      union {
        uint8_t reg_63;
      };
      union {
        struct {
          uint8_t io2_input_mode_configuration: 2;          // [64H(0), 801:800]
          uint8_t io2_output_mode_configuration: 2;         // [64H(2), 803:802]
          uint8_t io2_pull_up_down_resistance_selection: 2; // [64H(4), 805:804]
          uint8_t io2_pull_up_down_selection: 1;            // [64H(6), 806:806]
          uint8_t io2_output_enable: 1;                     // [64H(7), 807:807]
        };
        uint8_t reg_64;
      };
      union {
        struct {
          uint8_t io3_input_mode_configuration: 2;          // [65H(0), 809:808]
          uint8_t io3_output_mode_configuration: 2;         // [65H(2), 811:810]
          uint8_t io3_pull_up_down_resistance_selection: 2; // [65H(4), 813:812]
          uint8_t io3_pull_up_down_selection: 1;            // [65H(6), 814:814]
          uint8_t io3_output_enable: 1;                     // [65H(7), 815:815]
        };
        uint8_t reg_65;
      };
      union {
        struct {
          uint8_t io4_input_mode_configuration: 2;          // [66H(0), 817:816]
          uint8_t io4_output_mode_configuration: 2;         // [66H(2), 819:818]
          uint8_t io4_pull_up_down_resistance_selection: 2; // [66H(4), 821:820]
          uint8_t io4_pull_up_down_selection: 1;            // [66H(6), 822:822]
          uint8_t pad_02__: 1;
        };
        uint8_t reg_66;
      };
      union {
        struct {
          uint8_t io5_input_mode_configuration: 2;          // [67H(0), 825:824]
          uint8_t io5_output_mode_configuration: 2;         // [67H(2), 827:826]
          uint8_t io5_pull_up_down_resistance_selection: 2; // [67H(4), 829:828]
          uint8_t io5_pull_up_down_selection: 1;            // [67H(6), 830:830]
          uint8_t pad_03__: 1;
        };
        uint8_t reg_67;
      };
      union {
        struct {
          uint8_t : 1;                                      // [68H(0), 832:832]
          uint8_t scl_input_mode_configuration: 2;          // [68H(1), 834:833]
          uint8_t scl_pull_up_down_resistance_selection: 2; // [68H(3), 836:835]
          uint8_t pad_04__: 3;
        };
        uint8_t reg_68;
      };
      union {
        struct {
          uint8_t : 1;                                      // [69H(0), 840:840]
          uint8_t sda_input_mode_configuration: 2;          // [69H(1), 842:841]
          uint8_t sda_pull_up_down_resistance_selection: 2; // [69H(3), 844:843]
          uint8_t pad_05__: 3;
        };
        uint8_t reg_69;
      };
      union {
        struct {
          uint8_t : 2;                                      // [6AH(0), 849:848]
          uint8_t io6_output_mode_configuration: 2;         // [6AH(2), 851:850]
          uint8_t io6_pull_up_down_resistance_selection: 2; // [6AH(4), 853:852]
          uint8_t io6_pull_up_down_selection: 1;            // [6AH(6), 854:854]
          uint8_t io6_output_enable: 1;                     // [6AH(7), 855:855]
        };
        uint8_t reg_6a;
      };
      union {
        struct {
          uint8_t : 2;                                      // [6BH(0), 857:856]
          uint8_t io7_output_mode_configuration: 2;         // [6BH(2), 859:858]
          uint8_t io7_pull_up_down_resistance_selection: 2; // [6BH(4), 861:860]
          uint8_t io7_pull_up_down_selection: 1;            // [6BH(6), 862:862]
          uint8_t io7_output_enable: 1;                     // [6BH(7), 863:863]
        };
        uint8_t reg_6b;
      };
      union {
        struct {
          uint8_t io8_input_mode_configuration: 2;          // [6CH(0), 865:864]
          uint8_t io8_output_mode_configuration: 2;         // [6CH(2), 867:866]
          uint8_t io8_pull_up_down_resistance_selection: 2; // [6CH(4), 869:868]
          uint8_t io8_pull_up_down_selection: 1;            // [6CH(6), 870:870]
          uint8_t pad_06__: 1;
        };
        uint8_t reg_6c;
      };
      union {
        uint8_t reg_6d;
      };
      union {
        struct {
          uint8_t io9_input_mode_configuration: 2;          // [6EH(0), 881:880]
          uint8_t io9_output_mode_configuration: 2;         // [6EH(2), 883:882]
          uint8_t io9_pull_up_down_resistance_selection: 2; // [6EH(4), 885:884]
          uint8_t io9_pull_up_down_selection: 1;            // [6EH(6), 886:886]
          uint8_t pad_07__: 1;
        };
        uint8_t reg_6e;
      };
      union {
        struct {
          uint8_t io10_input_mode_configuration: 2;           // [6FH(0), 889:888]
          uint8_t io10_output_mode_configuration: 2;          // [6FH(2), 891:890]
          uint8_t io10_pull_up_down_resistance_selection: 2;  // [6FH(4), 893:892]
          uint8_t io10_pull_up_down_selection: 1;             // [6FH(6), 894:894]
          uint8_t pad_08__: 1;
        };
        uint8_t reg_6f;
      };
      union {
        struct {
          uint8_t io11_input_mode_configuration: 2;           // [70H(0), 897:896]
          uint8_t io11_output_mode_configuration: 2;          // [70H(2), 899:898]
          uint8_t io11_pull_up_down_resistance_selection: 2;  // [70H(4), 901:900]
          uint8_t io11_pull_up_down_selection: 1;             // [70H(6), 902:902]
          uint8_t pad_09__: 1;
        };
        uint8_t reg_70;
      };
      union {
        struct {
          uint8_t io12_input_mode_configuration: 2;           // [71H(0), 905:904]
          uint8_t io12_output_mode_configuration: 2;          // [71H(2), 907:906]
          uint8_t io12_pull_up_down_resistance_selection: 2;  // [71H(4), 909:908]
          uint8_t io12_pull_up_down_selection: 1;             // [71H(6), 910:910]
          uint8_t pad_10__: 1;
        };
        uint8_t reg_71;
      };
      union {
        struct {
          uint8_t io13_input_mode_configuration: 2;           // [72H(0), 913:912]
          uint8_t io13_output_mode_configuration: 2;          // [72H(2), 915:914]
          uint8_t io13_pull_up_down_resistance_selection: 2;  // [72H(4), 917:916]
          uint8_t io13_pull_up_down_selection: 1;             // [72H(6), 918:918]
          uint8_t pad_11__: 1;
        };
        uint8_t reg_72;
      };
      union {
        struct {
          uint8_t io14_input_mode_configuration: 2;           // [73H(0), 921:920]
          uint8_t io14_output_mode_configuration: 2;          // [73H(2), 923:922]
          uint8_t io14_pull_up_down_resistance_selection: 2;  // [73H(4), 925:924]
          uint8_t io14_pull_up_down_selection: 1;             // [73H(6), 926:926]
          uint8_t pad_12__: 1;
        };
        uint8_t reg_73;
      };
      union {
        struct {
          uint8_t : 1;                  // [74H(0), 928:928]
          uint8_t io0_digital_input: 1; // [74H(1), 929:929]
          uint8_t io1_digital_input: 1; // [74H(2), 930:930]
          uint8_t io2_digital_input: 1; // [74H(3), 931:931]
          uint8_t io3_digital_input: 1; // [74H(4), 932:932]
          uint8_t io4_digital_input: 1; // [74H(5), 933:933]
          uint8_t io5_digital_input: 1; // [74H(6), 934:934]
          uint8_t io8_digital_input: 1; // [74H(7), 935:935]
        };
        uint8_t reg_74;
      };
      union {
        struct {
          uint8_t io9_digital_input: 1;   // [75H(0), 936:936]
          uint8_t io10_digital_input: 1;  // [75H(1), 937:937]
          uint8_t io11_digital_input: 1;  // [75H(2), 938:938]
          uint8_t io12_digital_input: 1;  // [75H(3), 939:939]
          uint8_t io13_digital_input: 1;  // [75H(4), 940:940]
          uint8_t io14_digital_input: 1;  // [75H(5), 941:941]
          uint8_t lut2_0_dff0_out: 1;     // [75H(6), 942:942]
          uint8_t lut2_1_dff1_out: 1;     // [75H(7), 943:943]
        };
        uint8_t reg_75;
      };
      union {
        struct {
          uint8_t lut2_2_dff2_out: 1; // [76H(0), 944:944]
          uint8_t lut2_3_pgen_out: 1; // [76H(1), 945:945]
          uint8_t lut3_0_dff3_out: 1; // [76H(2), 946:946]
          uint8_t lut3_1_dff4_out: 1; // [76H(3), 947:947]
          uint8_t lut3_2_dff5_out: 1; // [76H(4), 948:948]
          uint8_t lut3_3_dff6_out: 1; // [76H(5), 949:949]
          uint8_t lut3_4_dff7_out: 1; // [76H(6), 950:950]
          uint8_t lut3_5_dff8_out: 1; // [76H(7), 951:951]
        };
        uint8_t reg_76;
      };
      union {
        struct {
          uint8_t lut3_6_pipedly_ripp_cnt_out0: 1;    // [77H(0), 952:952]
          uint8_t pipedly_ripp_cnt_out1: 1;           // [77H(1), 953:953]
          uint8_t ripp_cnt_out2: 1;                   // [77H(2), 954:954]
          uint8_t edet_filter_out: 1;                 // [77H(3), 955:955]
          uint8_t prog_dly_edet_out: 1;               // [77H(4), 956:956]
          uint8_t multfunc_8bit_1_dly_cnt_out: 1;     // [77H(5), 957:957]
          uint8_t ckosc1_matrix_osc1_matrix_input: 1; // [77H(6), 958:958]
          uint8_t ckosc0_matrix_osc0_matrix_input: 1; // [77H(7), 959:959]
        };
        uint8_t reg_77;
      };
      union {
        struct {
          uint8_t ckosc2_matrix_osc2_matrix_input: 1; // [78H(0), 960:960]
          uint8_t multfunc_8bit_2_dly_cnt_out: 1;     // [78H(1), 961:961]
          uint8_t multfunc_8bit_3_dly_cnt_out: 1;     // [78H(2), 962:962]
          uint8_t multfunc_8bit_4_dly_cnt_out: 1;     // [78H(3), 963:963]
          uint8_t multfunc_8bit_5_dly_cnt_out: 1;     // [78H(4), 964:964]
          uint8_t multfunc_8bit_6_dly_cnt_out: 1;     // [78H(5), 965:965]
          uint8_t multfunc_8bit_7_dly_cnt_out: 1;     // [78H(6), 966:966]
          uint8_t multfunc_16bit_0_lut_dff_out: 1;    // [78H(7), 967:967]
        };
        uint8_t reg_78;
      };
      union {
        struct {
          uint8_t multfunc_8bit_1_lut_dff_out: 1;   // [79H(0), 968:968]
          uint8_t multfunc_8bit_2_lut_dff_out: 1;   // [79H(1), 969:969]
          uint8_t multfunc_8bit_3_lut_dff_out: 1;   // [79H(2), 970:970]
          uint8_t multfunc_8bit_4_lut_dff_out: 1;   // [79H(3), 971:971]
          uint8_t multfunc_8bit_5_lut_dff_out: 1;   // [79H(4), 972:972]
          uint8_t multfunc_8bit_6_lut_dff_out: 1;   // [79H(5), 973:973]
          uint8_t multfunc_8bit_7_lut_dff_out: 1;   // [79H(6), 974:974]
          uint8_t multfunc_16bit_0_dly_cnt_out: 1;  // [79H(7), 975:975]
        };
        uint8_t reg_79;
      };
      union {
        struct {
          uint8_t virtual_input_7: 1; // [7AH(0), 976:976]
          uint8_t virtual_input_6: 1; // [7AH(1), 977:977]
          uint8_t virtual_input_5: 1; // [7AH(2), 978:978]
          uint8_t virtual_input_4: 1; // [7AH(3), 979:979]
          uint8_t virtual_input_3: 1; // [7AH(4), 980:980]
          uint8_t virtual_input_2: 1; // [7AH(5), 981:981]
          uint8_t virtual_input_1: 1; // [7AH(6), 982:982]
          uint8_t virtual_input_0: 1; // [7AH(7), 983:983]
        };
        uint8_t reg_7a;
      };
      union {
        struct {
          uint8_t : 1;                      // [7BH(0), 984:984]
          uint8_t : 1;                      // [7BH(1), 985:985]
          uint8_t acmp0l_out: 1;            // [7BH(2), 986:986]
          uint8_t acmp1l_out: 1;            // [7BH(3), 987:987]
          uint8_t second_ckosc1_matrix: 1;  // [7BH(4), 988:988]
          uint8_t second_ckosc0_matrix: 1;  // [7BH(5), 989:989]
          uint8_t por_core: 1;              // [7BH(6), 990:990]
          uint8_t pad_13__: 1;
        };
        uint8_t reg_7b;
      };
      union {
        struct {
          uint8_t cnt0_counted_value_7_0: 8; // [7CH(0), 999:992]
        };
        uint8_t reg_7c;
      };
      union {
        struct {
          uint8_t cnt0_counted_value_15_8: 8; // [7DH(0), 1007:1000]
        };
        uint8_t reg_7d;
      };
      union {
        struct {
          uint8_t cnt2_counted_value: 8; // [7EH(0), 1015:1008]
        };
        uint8_t reg_7e;
      };
      union {
        struct {
          uint8_t cnt4_counted_value: 8; // [7FH(0), 1023:1016]
        };
        uint8_t reg_7f;
      };
      union {
        struct {
          uint8_t osc1_turn_on_by_register: 1;            // [80H(0), 1024:1024]
          uint8_t osc1_matrix_power_down_or_on_select: 1; // [80H(1), 1025:1025]
          uint8_t osc1_external_clock_source_enable: 1;   // [80H(2), 1026:1026]
          uint8_t osc1_post_divider_ration_control: 2;    // [80H(3), 1028:1027]
          uint8_t osc1_matrix_divider_ratio_control: 3;   // [80H(5), 1031:1029]
        };
        uint8_t reg_80;
      };
      union {
        struct {
          uint8_t osc2_turn_on_by_register: 1;            // [81H(0), 1032:1032]
          uint8_t osc2_matrix_power_down_or_on_select: 1; // [81H(1), 1033:1033]
          uint8_t osc2_external_clock_source_enable: 1;   // [81H(2), 1034:1034]
          uint8_t osc2_post_divider_ration_control: 2;    // [81H(3), 1036:1035]
          uint8_t osc2_matrix_divider_ratio_control: 3;   // [81H(5), 1039:1037]
        };
        uint8_t reg_81;
      };
      union {
        struct {
          uint8_t osc0_turn_on_by_register: 1;            // [82H(0), 1040:1040]
          uint8_t osc0_matrix_power_down_or_on_select: 1; // [82H(1), 1041:1041]
          uint8_t osc0_external_clock_source_enable: 1;   // [82H(2), 1042:1042]
          uint8_t osc0_post_divider_ration_control: 2;    // [82H(3), 1044:1043]
          uint8_t osc0_matrix_divider_ratio_control: 3;   // [82H(5), 1047:1045]
        };
        uint8_t reg_82;
      };
      union {
        struct {
          uint8_t : 1;                            // [83H(0), 1048:1048]
          uint8_t osc0_matrix_out_enable: 1;      // [83H(1), 1049:1049]
          uint8_t osc1_matrix_out_enable: 1;      // [83H(2), 1050:1050]
          uint8_t osc2_matrix_out_enable: 1;      // [83H(3), 1051:1051]
          uint8_t osc2_100_ns_startup_delay: 1;   // [83H(4), 1052:1052]
          uint8_t osc0_2nd_matrix_out_enable: 1;  // [83H(5), 1053:1053]
          uint8_t osc1_2nd_matrix_out_enable: 1;  // [83H(6), 1054:1054]
          uint8_t pad_14__: 1;
        };
        uint8_t reg_83;
      };
      union {
        struct {
          uint8_t osc1_2nd_matrix_input_matrix_divider_ratio_control: 3; // [84H(0), 1058:1056]
          uint8_t osc0_2nd_matrix_input_matrix_divider_ratio_control: 3; // [84H(3), 1061:1059]
          uint8_t pad_15__: 2;
        };
        uint8_t reg_84;
      };
      union {
        uint8_t reg_85;
      };
      union {
        uint8_t reg_86;
      };
      union {
        struct {
          uint8_t : 1;                  // [87H(0), 1080:1080]
          uint8_t : 1;                  // [87H(1), 1081:1081]
          uint8_t acmp0l_hysteresis: 2; // [87H(2), 1083:1082]
          uint8_t pad_16__: 4;
        };
        uint8_t reg_87;
      };
      union {
        struct {
          uint8_t acmp1l_hysteresis: 2;                                               // [88H(0), 1089:1088]
          uint8_t : 1;                                                                // [88H(2), 1090:1090]
          uint8_t : 1;                                                                // [88H(3), 1091:1091]
          uint8_t acmp1l_positive_input_come_from_acmp0ls_input_mux_output_enable: 1; // [88H(4), 1092:1092]
          uint8_t pad_17__: 3;
        };
        uint8_t reg_88;
      };
      union {
        uint8_t reg_89;
      };
      union {
        uint8_t reg_8a;
      };
      union {
        struct {
          uint8_t acmp0l_gain_divider: 2; // [8BH(0), 1113:1112]
          uint8_t acmp0l_vref: 6;         // [8BH(2), 1119:1114]
        };
        uint8_t reg_8b;
      };
      union {
        struct {
          uint8_t acmp1l_gain_divider: 2; // [8CH(0), 1121:1120]
          uint8_t acmp1l_vref: 6;         // [8CH(2), 1127:1122]
        };
        uint8_t reg_8c;
      };
      union {
        struct {
          uint8_t : 1;                      // [8DH(0), 1128:1128]
          uint8_t : 2;                      // [8DH(1), 1130:1129]
          uint8_t vref_output_op: 1;        // [8DH(3), 1131:1131]
          uint8_t vref0_input_selection: 2; // [8DH(4), 1133:1132]
          uint8_t pad_18__: 2;
        };
        uint8_t reg_8d;
      };
      union {
        struct {
          uint8_t : 1;            // [8EH(0), 1136:1136]
          uint8_t : 1;            // [8EH(1), 1137:1137]
          uint8_t : 1;            // [8EH(2), 1138:1138]
          uint8_t vref_out_pd: 1; // [8EH(3), 1139:1139]
          uint8_t pad_19__: 4;
        };
        uint8_t reg_8e;
      };
      union {
        uint8_t reg_8f;
      };
      union {
        struct {
          uint8_t lut2_0_dff0_setting: 4; // [90H(0), 1155:1152]
          uint8_t lut2_1_dff1_setting: 4; // [90H(4), 1159:1156]
        };
        uint8_t reg_90;
      };
      union {
        struct {
          uint8_t lut2_2_dff2_setting: 4;     // [91H(0), 1163:1160]
          uint8_t lut2_3_val_or_pgen_data: 4; // [91H(4), 1167:1164]
        };
        uint8_t reg_91;
      };
      union {
        struct {
          uint8_t pgen_data_7_0: 8; // [92H(0), 1175:1168]
        };
        uint8_t reg_92;
      };
      union {
        struct {
          uint8_t pgen_data_15_8: 8; // [93H(0), 1183:1176]
        };
        uint8_t reg_93;
      };
      union {
        struct {
          uint8_t lut3_0_dff3_setting: 8; // [94H(0), 1191:1184]
        };
        uint8_t reg_94;
      };
      union {
        struct {
          uint8_t lut3_1_dff4_setting: 8; // [95H(0), 1199:1192]
        };
        uint8_t reg_95;
      };
      union {
        struct {
          uint8_t lut3_2_dff5_setting: 8; // [96H(0), 1207:1200]
        };
        uint8_t reg_96;
      };
      union {
        struct {
          uint8_t lut3_3_dff6_setting: 8; // [97H(0), 1215:1208]
        };
        uint8_t reg_97;
      };
      union {
        struct {
          uint8_t lut3_4_dff7_setting: 8; // [98H(0), 1223:1216]
        };
        uint8_t reg_98;
      };
      union {
        struct {
          uint8_t lut3_5_dff8_setting: 8; // [99H(0), 1231:1224]
        };
        uint8_t reg_99;
      };
      union {
        struct {
          uint8_t lut2_0_or_dff0_select: 1; // [9AH(0), 1232:1232]
          uint8_t lut2_1_or_dff1_select: 1; // [9AH(1), 1233:1233]
          uint8_t lut2_2_or_dff2_select: 1; // [9AH(2), 1234:1234]
          uint8_t lut2_3_or_pgen_select: 1; // [9AH(3), 1235:1235]
          uint8_t lut3_0_or_dff3_select: 1; // [9AH(4), 1236:1236]
          uint8_t dff3_secondq_sel: 1;      // [9AH(5), 1237:1237]
          uint8_t lut3_1_or_dff4_select: 1; // [9AH(6), 1238:1238]
          uint8_t lut3_2_or_dff5_select: 1; // [9AH(7), 1239:1239]
        };
        uint8_t reg_9a;
      };
      union {
        struct {
          uint8_t lut3_3_or_dff6_select: 1;             // [9BH(0), 1240:1240]
          uint8_t lut3_4_or_dff7_select: 1;             // [9BH(1), 1241:1241]
          uint8_t lut3_5_or_dff8_select: 1;             // [9BH(2), 1242:1242]
          uint8_t filter_or_edge_detector_selection: 1; // [9BH(3), 1243:1243]
          uint8_t output_polarity_select: 1;            // [9BH(4), 1244:1244]
          uint8_t select_the_edge_mode: 2;              // [9BH(5), 1246:1245]
          uint8_t pad_20__: 1;
        };
        uint8_t reg_9b;
      };
      union {
        struct {
          uint8_t lut_value_or_pipe_delay_out_sel_or_nset_end_value: 8; // [9CH(0), 1255:1248]
        };
        uint8_t reg_9c;
      };
      union {
        struct {
          uint8_t pipe_delay_out1_polarity_select: 1;                           // [9DH(0), 1256:1256]
          uint8_t lut3_6_or_pipe_delay_select: 1;                               // [9DH(1), 1257:1257]
          uint8_t pipe_ripp_cnt_s: 1;                                           // [9DH(2), 1258:1258]
          uint8_t select_the_edge_mode_of_programmable_delay_edge_detector: 2;  // [9DH(3), 1260:1259]
          uint8_t delay_value_select_for_programmable_delay_edge_detector: 2;   // [9DH(5), 1262:1261]
          uint8_t pad_21__: 1;
        };
        uint8_t reg_9d;
      };
      union {
        uint8_t reg_9e;
      };
      union {
        uint8_t reg_9f;
      };
      union {
        struct {
          uint8_t : 1;                        // [A0H(0), 1280:1280]
          uint8_t : 1;                        // [A0H(1), 1281:1281]
          uint8_t : 1;                        // [A0H(2), 1282:1282]
          uint8_t : 1;                        // [A0H(3), 1283:1283]
          uint8_t : 1;                        // [A0H(4), 1284:1284]
          uint8_t : 1;                        // [A0H(5), 1285:1285]
          uint8_t : 1;                        // [A0H(6), 1286:1286]
          uint8_t fsm0_set_rst_selection: 1;  // [A0H(7), 1287:1287]
        };
        uint8_t reg_a0;
      };
      union {
        struct {
          uint8_t lut4_0_dff9_setting_7_0: 8; // [A1H(0), 1295:1288]
        };
        uint8_t reg_a1;
      };
      union {
        struct {
          uint8_t lut4_0_dff9_setting_15_8: 8; // [A2H(0), 1303:1296]
        };
        uint8_t reg_a2;
      };
      union {
        struct {
          uint8_t dly_cnt0_mode_selection: 2;       // [A3H(0), 1305:1304]
          uint8_t dly_cnt0_edge_mode_selection: 2;  // [A3H(2), 1307:1306]
          uint8_t dly_cnt0_clock_source_select: 4;  // [A3H(4), 1311:1308]
        };
        uint8_t reg_a3;
      };
      union {
        struct {
          uint8_t cnt0_output_pol_selection: 1;         // [A4H(0), 1312:1312]
          uint8_t cnt0_initial_value_selection: 2;      // [A4H(1), 1314:1313]
          uint8_t : 1;                                  // [A4H(3), 1315:1315]
          uint8_t : 1;                                  // [A4H(4), 1316:1316]
          uint8_t keep_signal_sync_selection: 1;        // [A4H(5), 1317:1317]
          uint8_t up_signal_sync_selection: 1;          // [A4H(6), 1318:1318]
          uint8_t cnt0_dly_edet_function_selection: 1;  // [A4H(7), 1319:1319]
        };
        uint8_t reg_a4;
      };
      union {
        struct {
          uint8_t reg_cnt0_data_7_0: 8; // [A5H(0), 1327:1320]
        };
        uint8_t reg_a5;
      };
      union {
        struct {
          uint8_t reg_cnt0_data_15_8: 8; // [A6H(0), 1335:1328]
        };
        uint8_t reg_a6;
      };
      union {
        struct {
          uint8_t cnt0_cnt_mode_sync_selection: 1;  // [A7H(0), 1336:1336]
          uint8_t : 1;                              // [A7H(1), 1337:1337]
          uint8_t : 1;                              // [A7H(2), 1338:1338]
          uint8_t : 1;                              // [A7H(3), 1339:1339]
          uint8_t : 1;                              // [A7H(4), 1340:1340]
          uint8_t : 1;                              // [A7H(5), 1341:1341]
          uint8_t cnt1_initial_value_selection: 2;  // [A7H(6), 1343:1342]
        };
        uint8_t reg_a7;
      };
      union {
        struct {
          uint8_t lut3_7_dff10_setting: 8; // [A8H(0), 1351:1344]
        };
        uint8_t reg_a8;
      };
      union {
        struct {
          uint8_t dly_cnt1_clock_source_select: 4;          // [A9H(0), 1355:1352]
          uint8_t cnt1_function_and_edge_mode_selection: 4; // [A9H(4), 1359:1356]
        };
        uint8_t reg_a9;
      };
      union {
        struct {
          uint8_t reg_cnt1_data: 8; // [AAH(0), 1367:1360]
        };
        uint8_t reg_aa;
      };
      union {
        struct {
          uint8_t cnt1_output_pol_selection: 1;         // [ABH(0), 1368:1368]
          uint8_t : 1;                                  // [ABH(1), 1369:1369]
          uint8_t cnt1_cnt_mode_sync_selection: 1;      // [ABH(2), 1370:1370]
          uint8_t cnt1_dly_edet_function_selection: 1;  // [ABH(3), 1371:1371]
          uint8_t : 4;                                  // [ABH(4), 1375:1372]
        };
        uint8_t reg_ab;
      };
      union {
        struct {
          uint8_t lut3_8_dff_11_setting: 8; // [ACH(0), 1383:1376]
        };
        uint8_t reg_ac;
      };
      union {
        struct {
          uint8_t dly_cnt2_clock_source_select: 4;          // [ADH(0), 1387:1384]
          uint8_t cnt2_function_and_edge_mode_selection: 4; // [ADH(4), 1391:1388]
        };
        uint8_t reg_ad;
      };
      union {
        struct {
          uint8_t cnt2_initial_value_selection: 2;      // [AEH(0), 1393:1392]
          uint8_t : 1;                                  // [AEH(2), 1394:1394]
          uint8_t cnt2_output_pol_selection: 1;         // [AEH(3), 1395:1395]
          uint8_t : 1;                                  // [AEH(4), 1396:1396]
          uint8_t cnt2_cnt_mode_sync_selection: 1;      // [AEH(5), 1397:1397]
          uint8_t cnt2_dly_edet_function_selection: 1;  // [AEH(6), 1398:1398]
          uint8_t pad_22__: 1;
        };
        uint8_t reg_ae;
      };
      union {
        struct {
          uint8_t reg_cnt2_data: 8; // [AFH(0), 1407:1400]
        };
        uint8_t reg_af;
      };
      union {
        struct {
          uint8_t : 1;                              // [B0H(0), 1408:1408]
          uint8_t : 1;                              // [B0H(1), 1409:1409]
          uint8_t : 1;                              // [B0H(2), 1410:1410]
          uint8_t : 1;                              // [B0H(3), 1411:1411]
          uint8_t : 1;                              // [B0H(4), 1412:1412]
          uint8_t : 1;                              // [B0H(5), 1413:1413]
          uint8_t cnt3_initial_value_selection: 2;  // [B0H(6), 1415:1414]
        };
        uint8_t reg_b0;
      };
      union {
        struct {
          uint8_t lut3_9_dff12_setting: 8; // [B1H(0), 1423:1416]
        };
        uint8_t reg_b1;
      };
      union {
        struct {
          uint8_t dly_cnt3_clock_source_select: 4;          // [B2H(0), 1427:1424]
          uint8_t cnt3_function_and_edge_mode_selection: 4; // [B2H(4), 1431:1428]
        };
        uint8_t reg_b2;
      };
      union {
        struct {
          uint8_t reg_cnt3_data: 8; // [B3H(0), 1439:1432]
        };
        uint8_t reg_b3;
      };
      union {
        struct {
          uint8_t cnt3_output_pol_selection: 1;         // [B4H(0), 1440:1440]
          uint8_t : 1;                                  // [B4H(1), 1441:1441]
          uint8_t cnt3_cnt_mode_sync_selection: 1;      // [B4H(2), 1442:1442]
          uint8_t cnt3_dly_edet_function_selection: 1;  // [B4H(3), 1443:1443]
          uint8_t pad_27__: 4;
        };
        uint8_t reg_b4;
      };
      union {
        struct {
          uint8_t lut3_dff_setting: 8; // [B5H(0), 1455:1448]
        };
        uint8_t reg_b5;
      };
      union {
        struct {
          uint8_t dly_cnt4_clock_source_select: 4;          // [B6H(0), 1459:1456]
          uint8_t cnt4_function_and_edge_mode_selection: 4; // [B6H(4), 1463:1460]
        };
        uint8_t reg_b6;
      };
      union {
        struct {
          uint8_t cnt4_initial_value_selection: 2;      // [B7H(0), 1465:1464]
          uint8_t : 1;                                  // [B7H(2), 1466:1466]
          uint8_t cnt4_output_pol_selection: 1;         // [B7H(3), 1467:1467]
          uint8_t : 1;                                  // [B7H(4), 1468:1468]
          uint8_t cnt4_cnt_mode_sync_selection: 1;      // [B7H(5), 1469:1469]
          uint8_t cnt4_dly_edet_function_selection: 1;  // [B7H(6), 1470:1470]
          uint8_t pad_23__: 1;
        };
        uint8_t reg_b7;
      };
      union {
        struct {
          uint8_t reg_cnt4_data: 8; // [B8H(0), 1479:1472]
        };
        uint8_t reg_b8;
      };
      union {
        struct {
          uint8_t : 1;                              // [B9H(0), 1480:1480]
          uint8_t : 1;                              // [B9H(1), 1481:1481]
          uint8_t : 1;                              // [B9H(2), 1482:1482]
          uint8_t : 1;                              // [B9H(3), 1483:1483]
          uint8_t : 1;                              // [B9H(4), 1484:1484]
          uint8_t : 1;                              // [B9H(5), 1485:1485]
          uint8_t cnt5_initial_value_selection: 2;  // [B9H(6), 1487:1486]
        };
        uint8_t reg_b9;
      };
      union {
        struct {
          uint8_t lut3_11_dff14_setting: 8; // [BAH(0), 1495:1488]
        };
        uint8_t reg_ba;
      };
      union {
        struct {
          uint8_t dly_cnt5_clock_source_select: 4;          // [BBH(0), 1499:1496]
          uint8_t cnt5_function_and_edge_mode_selection: 4; // [BBH(4), 1503:1500]
        };
        uint8_t reg_bb;
      };
      union {
        struct {
          uint8_t reg_cnt5_data: 8; // [BCH(0), 1511:1504]
        };
        uint8_t reg_bc;
      };
      union {
        struct {
          uint8_t cnt5_output_pol_selection: 1;         // [BDH(0), 1512:1512]
          uint8_t : 1;                                  // [BDH(1), 1513:1513]
          uint8_t cnt5_cnt_mode_sync_selection: 1;      // [BDH(2), 1514:1514]
          uint8_t cnt5_dly_edet_function_selection: 1;  // [BDH(3), 1515:1515]
          uint8_t pad_24__: 4;
        };
        uint8_t reg_bd;
      };
      union {
        struct {
          uint8_t lut3_12_dff15_setting: 8; // [BEH(0), 1527:1520]
        };
        uint8_t reg_be;
      };
      union {
        struct {
          uint8_t dly_cnt6_clock_source_select: 4;          // [BFH(0), 1531:1528]
          uint8_t cnt6_function_and_edge_mode_selection: 4; // [BFH(4), 1535:1532]
        };
        uint8_t reg_bf;
      };
      union {
        struct {
          uint8_t cnt6_initial_value_selection: 2;      // [C0H(0), 1537:1536]
          uint8_t : 1;                                  // [C0H(2), 1538:1538]
          uint8_t cnt6_output_pol_selection: 1;         // [C0H(3), 1539:1539]
          uint8_t : 1;                                  // [C0H(4), 1540:1540]
          uint8_t cnt6_cnt_mode_sync_selection: 1;      // [C0H(5), 1541:1541]
          uint8_t cnt6_dly_edet_function_selection: 1;  // [C0H(6), 1542:1542]
          uint8_t pad_28__: 1;
        };
        uint8_t reg_c0;
      };
      union {
        struct {
          uint8_t reg_cnt6_data: 8; // [C1H(0), 1551:1544]
        };
        uint8_t reg_c1;
      };
      union {
        struct {
          uint8_t : 5;                              // [C2H(0), 1556:1552]
          uint8_t cnt7_output_pol_selection: 1;     // [C2H(5), 1557:1557]
          uint8_t : 1;                              // [C2H(6), 1558:1558]
          uint8_t cnt7_cnt_mode_sync_selection: 1;  // [C2H(7), 1559:1559]
        };
        uint8_t reg_c2;
      };
      union {
        struct {
          uint8_t lut3_13_dff16_setting: 8; // [C3H(0), 1567:1560]
        };
        uint8_t reg_c3;
      };
      union {
        struct {
          uint8_t dly_cnt7_clock_source_select: 4;          // [C4H(0), 1571:1568]
          uint8_t cnt7_function_and_edge_mode_selection: 4; // [C4H(4), 1575:1572]
        };
        uint8_t reg_c4;
      };
      union {
        struct {
          uint8_t cnt7_initial_value_selection: 2;      // [C5H(0), 1577:1576]
          uint8_t cnt7_dly_edet_function_selection: 1;  // [C5H(2), 1578:1578]
          uint8_t pad_25__: 5;
        };
        uint8_t reg_c5;
      };
      union {
        struct {
          uint8_t reg_cnt7_data: 8; // [C6H(0), 1591:1584]
        };
        uint8_t reg_c6;
      };
      union {
        struct {
          uint8_t io0_i2c_output_expander_data: 1;    // [C7H(0), 1592:1592]
          uint8_t io0_i2c_output_expander_select: 1;  // [C7H(1), 1593:1593]
          uint8_t io5_i2c_output_expander_data: 1;    // [C7H(2), 1594:1594]
          uint8_t io5_i2c_output_expander_select: 1;  // [C7H(3), 1595:1595]
          uint8_t io6_i2c_output_expander_data: 1;    // [C7H(4), 1596:1596]
          uint8_t io6_i2c_output_expander_select: 1;  // [C7H(5), 1597:1597]
          uint8_t io9_i2c_output_expander_data: 1;    // [C7H(6), 1598:1598]
          uint8_t io9_i2c_output_expander_select: 1;  // [C7H(7), 1599:1599]
        };
        uint8_t reg_c7;
      };
      union {
        struct {
          uint8_t : 1;                                                                // [C8H(0), 1600:1600]
          uint8_t i2c_reset_bit_with_reloading_nvm_into_data_register_soft_reset: 1;  // [C8H(1), 1601:1601]
          uint8_t io_latching_enable_during_i2c_write_interface: 1;                   // [C8H(2), 1602:1602]
          uint8_t pad_26__: 5;
        };
        uint8_t reg_c8;
      };
      union {
        struct {
          uint8_t i2c_write_mask_bits: 8; // [C9H(0), 1615:1608]
        };
        uint8_t reg_c9;
      };
      union {
        struct {
          uint8_t i2c_slave_address: 4;           // [CAH(0), 1619:1616]
          uint8_t slave_address_selection_a4: 1;  // [CAH(4), 1620:1620]
          uint8_t slave_address_selection_a5: 1;  // [CAH(5), 1621:1621]
          uint8_t slave_address_selection_a6: 1;  // [CAH(6), 1622:1622]
          uint8_t slave_address_selection_a7: 1;  // [CAH(7), 1623:1623]
        };
        uint8_t reg_ca;
      };
      union {
        struct {
          uint8_t pattern_id_byte_0: 8; // [CBH(0), 1631:1624]
        };
        uint8_t reg_cb;
      };
      union {
        uint8_t reg_cc;
      };
      union {
        uint8_t reg_cd;
      };
      union {
        uint8_t reg_ce;
      };
      union {
        uint8_t reg_cf;
      };
      union {
        uint8_t reg_d0;
      };
      union {
        uint8_t reg_d1;
      };
      union {
        uint8_t reg_d2;
      };
      union {
        uint8_t reg_d3;
      };
      union {
        uint8_t reg_d4;
      };
      union {
        uint8_t reg_d5;
      };
      union {
        uint8_t reg_d6;
      };
      union {
        uint8_t reg_d7;
      };
      union {
        uint8_t reg_d8;
      };
      union {
        uint8_t reg_d9;
      };
      union {
        uint8_t reg_da;
      };
      union {
        uint8_t reg_db;
      };
      union {
        uint8_t reg_dc;
      };
      union {
        uint8_t reg_dd;
      };
      union {
        uint8_t reg_de;
      };
      union {
        uint8_t reg_df;
      };
      union {
        struct {
          uint8_t register_read_selection_bits: 2;  // [E0H(0), 1793:1792]
          uint8_t register_write_selection_bits: 2; // [E0H(2), 1795:1794]
          uint8_t pad_29__: 4;
        };
        uint8_t reg_e0;
      };
      union {
        struct {
          uint8_t nvm_configuration_selection_bits: 2; // [E1H(0), 1801:1800]
          uint8_t pad_30__: 6;
        };
        uint8_t reg_e1;
      };
      union {
        struct {
          uint8_t : 2;                                // [E2H(0), 1809:1808]
          uint8_t write_protect_register_enable: 1;   // [E2H(2), 1810:1810]
          uint8_t : 5;                                // [E2H(3), 1815:1811]
        };
        uint8_t reg_e2;
      };
      union {
        struct {
          uint8_t page_selection_for_erase_erseb: 5;  // [E3H(0), 1820:1816]
          uint8_t : 1;                                // [E3H(5), 1821:1821]
          uint8_t : 1;                                // [E3H(6), 1822:1822]
          uint8_t erase_enable: 1;                    // [E3H(7), 1823:1823]
        };
        uint8_t reg_e3;
      };
      union {
        struct {
          uint8_t protection_lock_bit_prl: 1; // [E4H(0), 1824:1824]
          uint8_t pad_31__: 7;
        };
        uint8_t reg_e4;
      };
      union {
        uint8_t reg_e5;
      };
      union {
        uint8_t reg_e6;
      };
      union {
        uint8_t reg_e7;
      };
      union {
        uint8_t reg_e8;
      };
      union {
        uint8_t reg_e9;
      };
      union {
        uint8_t reg_ea;
      };
      union {
        uint8_t reg_eb;
      };
      union {
        uint8_t reg_ec;
      };
      union {
        uint8_t reg_ed;
      };
      union {
        uint8_t reg_ee;
      };
      union {
        uint8_t reg_ef;
      };
      union {
        uint8_t reg_f0;
      };
      union {
        uint8_t reg_f1;
      };
      union {
        uint8_t reg_f2;
      };
      union {
        uint8_t reg_f3;
      };
      union {
        uint8_t reg_f4;
      };
      union {
        uint8_t reg_f5;
      };
      union {
        uint8_t reg_f6;
      };
      union {
        uint8_t reg_f7;
      };
      union {
        uint8_t reg_f8;
      };
      union {
        uint8_t reg_f9;
      };
      union {
        uint8_t reg_fa;
      };
      union {
        uint8_t reg_fb;
      };
      union {
        uint8_t reg_fc;
      };
      union {
        uint8_t reg_fd;
      };
      union {
        uint8_t reg_fe;
      };
      union {
        uint8_t reg_ff;
      };

    };
    uint8_t reg_data[256];
  };
} slg_register_t;
